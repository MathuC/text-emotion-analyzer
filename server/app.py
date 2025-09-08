import os
from flask import Flask, jsonify, request

app = Flask(__name__, static_folder='../client/dist')

@app.route('/<path:filename>')
def serve_all(filename):
    return app.send_static_file(filename)

@app.route('/')
def serve():
    return app.send_static_file('index.html')

@app.route('/api', methods=['GET'])
def api():
    text = request.args.get("text", "undefined")
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)