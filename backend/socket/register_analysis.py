import logging

from flask_socketio import emit

logger = logging.getLogger(__name__)

def register_analysis(socketio):

    @socketio.on('analyse')
    def handle_analyse(message):
        print(f"Received message: {message}")
        # mp4 to mp3 start 0%
        emit('progress', "20", broadcast=True)

        # mp3 - 20%
        emit('progress', "40", broadcast=True)