from flask import Flask, request, send_file, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'packages'
USERS_FILE = 'users.json'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

@app.route('/')
def index():
    with open('templates/auth.html', 'r') as f:
        return f.read()

@app.route('/dashboard')
def dashboard():
    with open('templates/dashboard.html', 'r') as f:
        return f.read()

# Rest of the API routes remain the same
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    users = load_users()
    
    if data['username'] in users:
        return jsonify({'error': 'Username already exists'}), 400
        
    users[data['username']] = {
        'password': generate_password_hash(data['password']),
        'created_at': datetime.now().isoformat()
    }
    save_users(users)
    return jsonify({'status': 'success'}), 200

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    users = load_users()
    
    if data['username'] not in users or not check_password_hash(
        users[data['username']]['password'], data['password']):
        return jsonify({'error': 'Invalid credentials'}), 401
        
    return jsonify({'status': 'success'}), 200

@app.route('/api/send/<recipient>', methods=['POST'])
def send_package(recipient):
    users = load_users()
    if recipient not in users:
        return jsonify({'error': 'Recipient not found'}), 404
        
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
        
    file = request.files['file']
    sender = request.headers.get('X-User-ID', 'anonymous')
    
    recipient_dir = os.path.join(UPLOAD_FOLDER, recipient)
    os.makedirs(recipient_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{timestamp}_{secure_filename(file.filename)}"
    filepath = os.path.join(recipient_dir, filename)
    
    file.save(filepath)
    return jsonify({'status': 'success', 'filename': filename}), 200

@app.route('/api/receive/<user_id>', methods=['GET'])
def receive_packages(user_id):
    if user_id not in load_users():
        return jsonify({'error': 'User not found'}), 404
        
    user_dir = os.path.join(UPLOAD_FOLDER, user_id)
    if not os.path.exists(user_dir):
        return jsonify({'packages': []}), 200
        
    packages = os.listdir(user_dir)
    return jsonify({'packages': packages}), 200

@app.route('/api/download/<user_id>/<filename>', methods=['GET'])
def download_package(user_id, filename):
    if user_id not in load_users():
        return jsonify({'error': 'User not found'}), 404
        
    filepath = os.path.join(UPLOAD_FOLDER, user_id, filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(port=5000, debug=True)