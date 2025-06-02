from flask import Flask, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'timestamp': datetime.utcnow().isoformat() + 'Z'})

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('PORT', default=8080))