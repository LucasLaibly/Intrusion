from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck
from browser_history import generic
from browser_history.browsers import Firefox, Chrome, Safari

app = create('development')
profanity_checker = ProfanityCheck()


@app.route('/test', methods=['GET'])
def base():
    thisdict = {
        "0": "https://www.uranus.com",
        "1": "https://www.intrusion.io"
    }
    test = profanity_checker.is_dirty(thisdict)
    if test:
        return 'True'
    else:
        return 'False'


@app.route('/browser/<string:browser>', methods=['GET'])
def history(browser):
    if browser.lower() == 'firefox':
        thisdict = {
            "0": "https://www.uranus.com",
            "1": "https://www.intrusion.io"
        }

        print(thisdict)
        return 'true'

    else:
        return 'No browser set'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
