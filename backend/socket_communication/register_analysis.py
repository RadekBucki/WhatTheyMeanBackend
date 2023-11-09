import logging
import string

from flask_socketio import emit

from backend.ai import process_audio, transcribe, sum_up, run_sentiment_analysis
from backend.video_parser.YouTubeDownloader import YouTubeDownloader

logger = logging.getLogger(__name__)


def register_analysis(socketio):

#service

    @socketio.on('analyse')
    def handle_analyse(analyse_uuid: string):
        logger.info(f"Received analyse: {analyse_uuid}")
        analyse = {
            "url": "https://www.youtube.com/watch?v=NxHrTaWzAL4"
        }
        # analyse = service.get_analyse(analyse_uuid)

        base64_file = None
        if analyse['url']:
            base64_file = YouTubeDownloader.download(analyse['url'])
        emit('progress', "20", broadcast=True)

        processing_dto = process_audio(base64_file)
        logger.info(f"Processing result: {processing_dto.sentiment}")
        emit('progress', "100", broadcast=True)