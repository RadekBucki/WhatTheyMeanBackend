import logging

from flask_socketio import emit

logger = logging.getLogger(__name__)


def register_socketio_events(socketio):
    @socketio.on('connect')
    def on_connect():
        logger.info("Connected")
        emit('after connect', "Connected successfully")

    @socketio.on('disconnect')
    def on_disconnect():
        logger.info("Disconnected")
        emit('after disconnect', "Disconnected successfully")
