from flask import Flask, jsonify
import datetime
import socket 

app = Flask(__name__)

# Root route - helpful for basic health checks or browser visits
@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome to the Flask API. Try /api/v1/details or /api/v1/healthz.'
    })

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'This is a simple Flask API for demonstration purposes-10.'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'up'
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
