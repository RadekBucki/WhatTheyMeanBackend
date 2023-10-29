import logging

from flask import Flask
from flask_socketio import SocketIO

from backend.api.routes import api
from backend.socket.register_analysis import register_analysis
from backend.socket.register_socket import register_socketio_events

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins="*")

# Set up logging
logging.basicConfig(level=logging.DEBUG, force=True)

# Register the routes
app.register_blueprint(api)

# Register the socketio events
register_socketio_events(socketio)
register_analysis(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)
