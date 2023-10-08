# app.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with your secret key
socketio = SocketIO(app)

users = {}
chat_history = []


@app.route('/')
def index():
    return jsonify({'success': True, 'message': 'Connected'})


@app.route('/register', methods=['POST'])
def register():
    return jsonify({'success': True, 'message': 'Registration successful'})


@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    chat_history.append({'username': username, 'message': message})
    emit('message', {'username': username, 'message': message}, broadcast=True)


@socketio.on('connect')
def handle_connect():
    emit('update_users', list(users.keys()))


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
