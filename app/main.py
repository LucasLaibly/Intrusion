from app.src.server import create
from app.src.profanity.profanity_check import ProfanityCheck
from browser_history.browsers import Firefox, Chrome, Safari

app = create('development')
profanity_checker = ProfanityCheck()


@app.route('/lobby', methods=['GET'])
def base():
    this_dict = {
        "0": "https://www.uranus.com",
        "1": "https://www.intrusion.io",
        "2": "https://www.myanus.com",
        "3": "https://www.uranus.com"
    }
    test = profanity_checker.is_dirty(this_dict)
    print(test)
    if test:
        return 'True'
    else:
        return 'False'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
