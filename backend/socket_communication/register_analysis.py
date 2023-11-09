import logging
import string

from flask_socketio import emit

logger = logging.getLogger(__name__)


def register_analysis(socketio):

    @socketio.on('analyse')
    def handle_analyse(analyse_uuid: string):
        logger.info(f"Received analyse: {analyse_uuid}")

        # file to mp3 start -> completed 10%
        emit('progress', "20", broadcast=True)

        # mp3 -> text start -> completed 30%
        emit('progress', "30", broadcast=True)

        emit('completed', analyse_uuid, broadcast=True)