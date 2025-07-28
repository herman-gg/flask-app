from flask import Flask, jsonify, render_template
from datetime import datetime
import os
import socket

app = Flask(__name__)

def get_status_data():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    status_data = {
        'timestamp': datetime.utcnow().isoformat() + 'Z',
        'pod': os.getenv('POD_NAME', default='None'),
        'ip': f'{hostname} : {ip}',
    }
    return status_data

@app.route('/status', methods=['GET'])
def status():
    return jsonify(get_status_data())

@app.route('/', methods=['GET'])
def index():
    data = get_status_data()
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', default=8080))