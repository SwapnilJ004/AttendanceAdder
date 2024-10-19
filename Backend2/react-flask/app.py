import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Define the upload folder path
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')

# Ensure the folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def get_next_filename():
    """Helper function to find the next available Attendance[i] filename."""
    files = os.listdir(UPLOAD_FOLDER)
    
    # Filter files that start with 'Attendance' and have a number followed by a file extension
    attendance_files = [f for f in files if f.startswith("Attendance") and f[10:f.rfind('.')].isdigit()]
    
    # Extract numbers from filenames like Attendance1, Attendance2, etc.
    numbers = [int(f[10:f.rfind('.')]) for f in attendance_files if f[10:f.rfind('.')].isdigit()]

    # Find the next available number
    next_number = max(numbers, default=0) + 1  # Get the next number
    return f"Attendance{next_number}"


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
        return jsonify({"message": f"File uploaded successfully as {new_filename}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
