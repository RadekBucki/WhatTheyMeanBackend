import logging
import os

from flask import Flask
from flask.cli import load_dotenv
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

from backend.api.exception_handlers import handle_500_error, handle_bad_request
from backend.api.routes import api
from backend.socket.register_analysis import register_analysis
from backend.socket.register_socket import register_socketio_events

app = Flask(__name__)
app.debug = True
socketio = SocketIO(app, cors_allowed_origins="*")

# Set up logging
logging.basicConfig(level=logging.DEBUG, force=True)

# Connect to database
load_dotenv()
app.config["MONGO_URI"] = os.getenv('MONGO_DB_URI')
mongo = PyMongo(app)
db = mongo.db

# Register the routes
app.register_blueprint(api)
app.register_error_handler(500, handle_500_error)
app.register_error_handler(Exception, handle_bad_request)

# Register the socketio events
register_socketio_events(socketio)
register_analysis(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)
