from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

# Dummy data store
current_data = {
    'ambulance_detected': False,
    'gps': {'lat': 0.0, 'lng': 0.0},
    'signal': 'RED'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_gps', methods=['POST'])
def update_gps():
    data = request.get_json()
    current_data['gps'] = data
    return jsonify({"message": "GPS updated"}), 200

@app.route('/update_signal', methods=['POST'])
def update_signal():
    data = request.get_json()
    current_data['signal'] = data['signal']
    return jsonify({"message": "Signal updated"}), 200

@app.route('/update_detection', methods=['POST'])
def update_detection():
    data = request.get_json()
    current_data['ambulance_detected'] = data['detected']
    return jsonify({"message": "Detection status updated"}), 200

@app.route('/data')
def get_data():
    return jsonify(current_data)

if __name__ == '__main__':
    app.run(debug=True)
