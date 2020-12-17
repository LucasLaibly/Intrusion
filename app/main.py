from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck

app = create('development')
profanity_checker = ProfanityCheck()


@app.route('/test/<string:word>', methods=['GET', 'POST'])
def base(word):
    test = profanity_checker.is_dirty(word)
    if test:
        return 'True'
    else:
        return 'False'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
