from flask import Flask, Blueprint
from flask_restful import Api

def create_app():

    flask_app = Flask(__name__)

    # When we need a config a file
    # flask_app.config.from_pyfile('config.py')

    # blueprint
    bp = Blueprint('api', __name__, static_url_path="assets")

    # api
    api = Api(bp)

    @app.route('/')
    def index():
        return 'Welcome to the Flask app'

    return flask_app

app = create_app()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)