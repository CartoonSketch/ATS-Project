from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import random
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='static', template_folder='templates')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dummy data store
current_data = {
    'ambulance_detected': False,
    'gps': {'lat': 0.0, 'lng': 0.0},
    'signal': 'RED'
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400

    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(video_path)

        # Run ambulance detection (YOLOv5 or script) on this video
        # Modify this command according to your model's script
        try:
            result = subprocess.run(['python3', 'ambulance_detector.py', '--video', video_path], capture_output=True, text=True)
            print(result.stdout)
            print(result.stderr)
        except Exception as e:
            return jsonify({'error': f'Error running detector: {str(e)}'}), 500

        return jsonify({'message': 'Video uploaded and processed successfully'})
    else:
        return jsonify({'error': 'Invalid file type'}), 400

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
