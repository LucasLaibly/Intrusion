from flask import jsonify
from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

from browser_history.browsers import Firefox, Chrome, Safari

profanity_checker = ProfanityCheck()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

socketio = SocketIO(app)


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
    emit('my response', {'data': 'Connected'})


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    # respond
    send(data)


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


if __name__ == "__main__":
    socketio.run(app, host='127.0.0.1', port=5000, cors_allowed_origins='*')
