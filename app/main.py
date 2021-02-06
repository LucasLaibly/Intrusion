from flask import jsonify
from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck
from app.src.socials.socials_check import SocialCheck
from browser_history.browsers import Firefox, Chrome, Safari

app = create('development')
profanity_checker = ProfanityCheck()
social_checker = SocialCheck()


@app.route('/user', methods=['GET'])
def base():
    this_dict = {
        "0": "https://www.instagram.com/LucasLaibly",
        "1": "https://www.facebook.com",
        "2": "https://www.instagram.com/something",
        "3": "https://www.twitter.com/home",
        "4": "https://www.chess.com"
    }
    # response = profanity_checker.is_dirty(this_dict)
    response = social_checker.find_origin(this_dict)

    if response:
        return jsonify(response)
    else:
        return jsonify(response)


@app.route('/censor/<string:word>')
def add_word(word):
    profanity_checker.add_word(word)
    return 'Added word!'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
