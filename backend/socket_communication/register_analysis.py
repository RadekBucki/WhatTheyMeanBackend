import base64
import logging
from typing import Dict

from bson import ObjectId
from flask_socketio import emit

from backend.ai.processing import transcribe, sum_up, run_sentiment_analysis
from backend.database.database_service import DataBaseService
from backend.exceptions.illegal_argument_exception import IllegalArgumentException
from backend.model.analysis import Analysis
from backend.model.author_attitude import AuthorAttitude
from backend.model.file_type import FileType
from backend.model.status import Status
from backend.video_parser.TikTokDownloader import TikTokDownloader
from backend.video_parser.YouTubeDownloader import YouTubeDownloader

logger: logging.Logger = logging.getLogger(__name__)


def register_analysis(socketio):
    @socketio.on('analyse')
    def handle_analyse(analyse_uuid: str):
        try:
            logger.info(f"Received analyse uuid: {analyse_uuid}")
            analyze: Analysis = DataBaseService.get_analysis_by_uuid(ObjectId(analyse_uuid))

            base64_file: str = ''
            if analyze.link:
                base64_file = download_file(analyse_uuid, analyze.link)

            else:
                DataBaseService.update_analysis_by_id(uuid=analyse_uuid, file_type=FileType.RAW)
                base64_file = base64.b64encode(analyze.raw_file).decode()
            emit('progress', "20")

            transcription = transcribe(base64_file)
            emit('progress', "40")

            summary = sum_up(transcription)
            emit('progress', "60")

            sentiment = run_sentiment_analysis(transcription)
            emit('progress', "80")

            DataBaseService.update_analysis_by_id(uuid=analyse_uuid,
                                                  status=Status.SUCCESS,
                                                  full_transcription=transcription,
                                                  video_summary=summary,
                                                  raw_file=base64_file,
                                                  author_attitude=get_sentiment_label(sentiment))
            emit('progress', "100")
            emit('done')

        except Exception as e:
            logger.error(f"Error while processing analysis: {e}")
            emit('failed', str(e))
            DataBaseService.update_analysis_by_id(uuid=analyse_uuid, status=Status.FAILED)

    def download_file(analyse_uuid, link: str) -> str:
        if "youtube" in link:
            DataBaseService.update_analysis_by_id(uuid=analyse_uuid, file_type=FileType.YOUTUBE)
            return YouTubeDownloader.download(link)
        elif "tiktok" in link:
            DataBaseService.update_analysis_by_id(uuid=analyse_uuid, file_type=FileType.TIKTOK)
            return TikTokDownloader.download(link)
        else:
            raise IllegalArgumentException("Link is not supported")

    def get_sentiment_label(sentiment_scores: Dict[str, float]) -> str:
        max_key = max(sentiment_scores, key=sentiment_scores.get)
        matching_attitude = next(attitude for attitude in AuthorAttitude if max_key in attitude.value)
        return matching_attitude
