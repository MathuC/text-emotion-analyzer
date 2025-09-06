import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder='../client/dist')

# since npm run build puts the react build into assets folder
@app.route('/assets/<path:filename>')
def serve_static(filename):
    return app.send_static_file(f'assets/{filename}')

@app.route('/')
def serve():
    return app.send_static_file('index.html')

@app.route('/api', methods=['GET'])
def api():
    text = request.args.get("text", "undefined")
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)