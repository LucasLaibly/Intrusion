from flask import Flask, jsonify
import browserhistory as bh

server = Flask(__name__)

@server.route('/')
def hello():
    return "Server is running..."

@server.route('/history')
def history():
    dict_obj = bh.get_browserhistory()

    dict_obj.keys()

    return jsonify(dict_obj)


if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000)