import logging

from flask_socketio import emit

from backend.video_parser.YouTubeDownloader import YouTubeDownloader

logger = logging.getLogger(__name__)


def register_socketio_events(socketio):

    @socketio.on('connect')
    def on_connect():
        logger.info("Connected")
        YouTubeDownloader.download("https://www.youtube.com/watch?v=SzWv8WD0Sik")
        emit('after connect', "Connected successfully", broadcast=True)

    @socketio.on('disconnect')
    def on_disconnect():
        logger.info("Disconnected")
        emit('after disconnect', "Disconnected successfully", broadcast=True)