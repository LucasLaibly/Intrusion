import eventlet
eventlet.monkey_patch()

from app.src.profanity.profanity_check import ProfanityCheck
from flask import Flask, render_template
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_socketio import send, emit
from flask_socketio import join_room, leave_room
from browser_history.browsers import Firefox, Chrome, Safari

profanity_checker = ProfanityCheck()

app = Flask(__name__)
# all domains on all routes: https://flask-cors.readthedocs.io/en/latest/
CORS(app)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/user', methods=['GET'])
def base():
    this_dict = {
        "0": "https://www.uranus.com",
        "1": "https://www.intrusion.io",
        "2": "https://www.myanus.com",
        "3": "https://www.uranus.com",
        "4": "https://www.chess.com"
    }
    response = profanity_checker.is_dirty(this_dict)

    if response:
        return jsonify(response)
    else:
        return jsonify(response)


@app.route('/censor/<string:word>')
def add_word(word):
    profanity_checker.add_word(word)
    return 'Added word!'


@socketio.on('connect')
def test_connect():
    print('Connected')
    emit('my response', {'data': 'Connected'})


@socketio.on('disconnect')
def test_disconnect():
    print('Disconnected')
    emit('my response', {'data': 'Disconnected'})


def ack():
    print('message was received!')


@socketio.on('join')
def on_join(data):
    # Since all clients are assigned a personal room, to address a message to a single client,
    # the session ID of the client can be used as the room argument.
    username = data['username']
    room = data['room']
    join_room(room)

    print(username + ' has entered the room.')
    emit('message', username + ' has entered the room.', room=room, callback=ack)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)

    print(username + ' has left the room.')
    emit('message', username + ' has left the room.', room=room, callback=ack)


@socketio.on_error()  # Handles the default namespace
def error_handler(e):
    pass


@socketio.on_error_default  # handles all namespaces without an explicit error handler
def default_error_handler(e):
    pass


if __name__ == "__main__":
    socketio.run(app, host='127.0.0.1', port=5000)
