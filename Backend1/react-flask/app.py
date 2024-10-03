from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS  # Import CORS
import os
import convertapi

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Set upload folder
app.config['UPLOAD_FOLDER'] = './uploads'
convertapi.api_secret = 'secret_dNB0v09AfZ2yOwUe'

# Ensure upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/api/upload', methods=['POST'])
def upload_file():
    print("API Route Hit")  # Check if API is hit

    if 'file' not in request.files:
        print("No file part in request")  # Debugging: No file found
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    print(f"File received: {file.filename}")  # Debugging: File received

    if file.filename == '':
        print("No selected file")  # Debugging: No filename
        return jsonify({'error': 'No selected file'}), 400

    if file and file.filename.endswith('.pdf'):
        print(f"File is PDF: {file.filename}")  # Debugging: File is PDF
        filename = secure_filename(file.filename)
        print(f"Secure Filename: {filename}")  # Debugging: Secure filename
        
        # Check if filename is valid and not None
        if not filename:
            print("Invalid filename")  # Debugging: Invalid filename
            return jsonify({'error': 'Invalid filename'}), 400

        # filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        filepath = os.path.join('./', filename)

        print(f"Saving file at: {filepath}")  # Debugging: Filepath
        
        # Save the file
        try:
            file.save(filepath)
            print(f"File saved at: {filepath}")  # Debugging: File saved
        except Exception as e:
            print(f"Error saving file: {str(e)}")  # Debugging: Error while saving
            return jsonify({'error': f"Error saving file: {str(e)}"}), 500

        # Check if filepath exists and is valid
        if not os.path.exists(filepath):
            print(f"File {filepath} does not exist")  # Debugging: File doesn't exist
            return jsonify({'error': f"File {filepath} does not exist"}), 400

        try:
            print(f"Starting conversion of {filepath}")  # Debugging: Start conversion
            convertapi.convert('xlsx', {
                'File': 'Btech_Attendance_2024.pdf'
            }, from_format='pdf').save_files('./')

        except Exception as e:
            print(f"ConvertAPI error: {str(e)}")  # Error handling

        print(f"File converted and saved successfully at {app.config['UPLOAD_FOLDER']}")  # Debugging: Conversion success

        return jsonify({'message': 'File uploaded and converted successfully!'}), 200

    print("File format not supported")  # Debugging: Unsupported file format
    return jsonify({'error': 'File format not supported'}), 400

if __name__ == '__main__':
    app.run(debug=True)
