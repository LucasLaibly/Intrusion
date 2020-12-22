from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck
from browser_history import generic
from browser_history.browsers import Firefox, Chrome, Safari

app = create('development')
profanity_checker = ProfanityCheck()


@app.route('/test/<string:word>', methods=['GET', 'POST'])
def base(word):
    test = profanity_checker.is_dirty(word)
    if test:
        return 'True'
    else:
        return 'False'


@app.route('/browser/<string:browser>', methods=['GET'])
def history(browser):
    if browser.lower() == 'firefox':
        f = Firefox()
        his = f.fetch().get()

        print(dict(his))
        return 'true'

    elif browser.lower() == 'chrome':
        c = Chrome()

    elif browser.lower() == 'safari':
        return 'Get a real browser ... that we can use please.'

    else:
        return 'No browser set'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
