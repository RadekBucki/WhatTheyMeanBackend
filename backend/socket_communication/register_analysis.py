import logging

from bson import ObjectId
from flask_socketio import emit

from backend.ai.processing import Processing, transcribe, sum_up, run_sentiment_analysis
from backend.database.database_service import DataBaseService
from backend.model.analysis import Analysis
from backend.model.file_type import FileType
from backend.model.status import Status
from backend.video_parser.YouTubeDownloader import YouTubeDownloader

logger: logging.Logger = logging.getLogger(__name__)
processing: Processing = Processing()

def register_analysis(socketio):

    @socketio.on('analyse')
    def handle_analyse(analyse_uuid: dict):
        uuid = analyse_uuid["text"]
        logger.info(f"Received analyse uuid: {uuid}")
        analyze: Analysis = DataBaseService.get_analysis_by_uuid(ObjectId(uuid))

        try:
            DataBaseService.update_analysis_by_id(uuid=analyse_uuid, status=Status.IN_PROGRESS)

            base64_file: str = ''
            if analyze.link:
                base64_file = YouTubeDownloader.download(analyze.link)
                DataBaseService.update_analysis_by_id(uuid=analyse_uuid, file_type=FileType.YOUTUBE)
            else:
                DataBaseService.update_analysis_by_id(uuid=analyse_uuid, file_type=FileType.RAW)
                base64_file = str(analyze.raw_file)
            emit('progress', "20", broadcast=True)

            transcription = transcribe(base64_file)
            emit('progress', "40", broadcast=True)

            summary = sum_up(transcription)
            emit('progress', "60", broadcast=True)

            sentiment = run_sentiment_analysis(transcription)
            emit('progress', "80", broadcast=True)

            DataBaseService.update_analysis_by_id(uuid=analyse_uuid,
                                                  status=Status.SUCCESS,
                                                  full_transcription=transcription,
                                                  video_summary=summary,
                                                  raw_file=base64_file,
                                                  author_attitude=sentiment)
            emit('progress', "100", broadcast=True)
            emit('done', broadcast=True)

        except Exception as e:
            logger.error(f"Error while processing analysis: {e}")
            DataBaseService.update_analysis_by_id(uuid=analyse_uuid, status=Status.FAILED)
            emit('failed', broadcast=True)