import os
import subprocess
import time
from flask_cors import CORS
from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Ensure the uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Ensure the outputs folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def get_next_filename():
    """
    Generate the next filename in the form of 'Attendance[i].ext',
    where i is the next available number and .ext is the extension of the uploaded file.
    """
    existing_files = os.listdir(UPLOAD_FOLDER)
    attendance_files = [f for f in existing_files if f.startswith('Attendance') and f.endswith('.csv')]  # Modify if using other extensions

    if attendance_files:
        # Extract the numbers from filenames like 'Attendance1.csv' and find the max
        numbers = [int(f.replace('Attendance', '').split('.')[0]) for f in attendance_files]
        next_number = max(numbers) + 1
    else:
        next_number = 1  # If no files exist, start from 1

    return f'Attendance{next_number}'


@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Generate the next available Attendance[i] filename
        new_filename = get_next_filename() + os.path.splitext(file.filename)[1]  # Retain the original file extension
        file_path = os.path.join(UPLOAD_FOLDER, new_filename)
        # Save the file in the uploads folder
        file.save(file_path)
        
        # Run Core.py after saving the file
        try:
            subprocess.run(['python', 'Core.py'], check=True)  # This will run Core.py
        except subprocess.CalledProcessError as e:
            return jsonify({"error": f"Core.py execution failed: {e}"}), 500
        
        return jsonify({"message": "File uploaded and processing started"}), 200


@app.route('/api/processed-file', methods=['GET'])
def check_processed_file():
    output_file = get_latest_output_file()
    if output_file:
        return jsonify({"output_file": output_file}), 200
    else:
        return jsonify({"output_file": None}), 202  # File still processing


def get_latest_output_file():
    # Helper function to check the output folder for the latest file
    output_files = os.listdir(OUTPUT_FOLDER)
    if output_files:
        latest_output = max(output_files, key=lambda f: os.path.getctime(os.path.join(OUTPUT_FOLDER, f)))
        return latest_output
    return None


@app.route('/api/output/<filename>', methods=['GET'])
def download_output_file(filename):
    return send_from_directory(OUTPUT_FOLDER, filename)


if __name__ == '__main__':
    app.run(debug=True)
