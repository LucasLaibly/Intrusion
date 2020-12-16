from flask import Flask
from flask_restful import Api
from app.src.server import create

app = create('development')


@app.route('/test')
def base():
    return 'route one'


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
