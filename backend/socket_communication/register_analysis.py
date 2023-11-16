import logging

from bson import ObjectId
from flask_socketio import emit

from backend.ai.processing import Processing
from backend.database.database_service import DataBaseService
from backend.model.analysis import Analysis
from backend.model.status import Status
from backend.video_parser.YouTubeDownloader import YouTubeDownloader

logger: logging.Logger = logging.getLogger(__name__)
processing: Processing = Processing()

def register_analysis(socketio):

    @socketio.on('analyse')
    def handle_analyse(analyse_uuid: ObjectId):
        logger.info(f"Received analyse uuid: {analyse_uuid}")
        analyze: Analysis = DataBaseService.get_analysis_by_id(analyse_uuid)

        if analyze.link:
            base64_file = YouTubeDownloader.download(analyze.link)
            DataBaseService.update_analysis_by_id(uuid=analyse_uuid, raw_file=base64_file)
        DataBaseService.update_analysis_by_id(uuid=analyse_uuid, status=Status.IN_PROGRESS)
        emit('progress', "20", broadcast=True)

        #
        #
        #
        #
        # processing_dto = process_audio(base64_file)
        # logger.info(f"Processing result: {processing_dto.sentiment}")
        # emit('progress', "100", broadcast=True)