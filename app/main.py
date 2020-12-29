from flask import jsonify
from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck
from browser_history.browsers import Firefox, Chrome, Safari

app = create('development')
profanity_checker = ProfanityCheck()


@app.route('/user', methods=['GET'])
def base():
    this_dict = {
        "0": "https://www.uranus.com",
        "1": "https://www.intrusion.io",
        "2": "https://www.myanus.com",
        "3": "https://www.uranus.com",
        "4": "https://www.chess.com"
    }
    test = profanity_checker.is_dirty(this_dict)

    if test:
        return jsonify(test)
    else:
        return jsonify(test)


@app.route('/censor/<string:word>')
def add_word(word):
    profanity_checker.add_word(word)
    return 'Added word!'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
