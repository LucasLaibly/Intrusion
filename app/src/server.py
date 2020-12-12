from flask import Flask, jsonify
from flask_RESTful import Api

server = Flask(__name__)

@server.route('/')
def hello():
    return "Server is running..."



if __name__ == "__main__":
    server.run(host='127.0.0.1', port=5000)