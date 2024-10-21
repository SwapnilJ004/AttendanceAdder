import React, { useState, useEffect } from 'react';
import { Box, Button, Typography, CircularProgress } from '@mui/material';
import axios from 'axios';

function AttendanceList() {
  const [loading, setLoading] = useState(false);  // Show processing spinner only after upload
  const [outputFile, setOutputFile] = useState(null); // For storing the output file from backend
  const [file, setFile] = useState(null); // To track uploaded file
  const [uploading, setUploading] = useState(false); // To track the upload process

  // Handles file upload
  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      alert('Please select a file first.');
      return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    setUploading(true);

    try {
      // Upload file to the backend
      await axios.post('http://127.0.0.1:5000/api/upload', formData);
      setUploading(false);
      setLoading(true);  // Start showing the spinner for processing after upload
      checkFileProcessing();  // Start polling for the processed file
    } catch (error) {
      console.error('Error uploading file:', error);
      setUploading(false);
    }
  };

  // Polling the backend to check for processed file
  const checkFileProcessing = async () => {
    try {
      let isFileReady = false;
      while (!isFileReady) {
        const response = await axios.get('http://127.0.0.1:5000/api/processed-file');
        
        // If the file is not yet processed, keep waiting
        if (response.status === 202) {
          console.log("File is still processing...");
          await new Promise(resolve => setTimeout(resolve, 3000)); // Wait for 3 seconds before checking again
        } else if (response.status === 200 && response.data.output_file) {
          setOutputFile(response.data.output_file);  // Set the output file from backend response
          isFileReady = true;
        }
      }
      setLoading(false);  // Hide loading spinner after processing
    } catch (error) {
      console.error('Error fetching processed file:', error);
      setLoading(false);  // In case of error, hide spinner
    }
  };

  // Handles file download
  const handleDownload = () => {
    if (outputFile) {
      const link = document.createElement('a');
      link.href = `http://127.0.0.1:5000/api/output/${outputFile}`;
      link.setAttribute('download', outputFile); // Filename for download
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);
    }
  };

  return (
    <Box mt={5} textAlign="center">
      <Typography variant="h4">Attendance List</Typography>

      {/* Show a file upload prompt if no file has been uploaded */}
      {!file && (
        <Box mt={3}>
          <Typography variant="h6" mt={2}>Upload a file to get started</Typography>
          <input type="file" onChange={handleFileChange} />
          <Button 
            variant="contained" 
            color="primary" 
            onClick={handleUpload} 
            disabled={uploading}
          >
            {uploading ? 'Uploading...' : 'Upload File'}
          </Button>
        </Box>
      )}

      {/* Show processing spinner while the file is being processed */}
      {loading && (
        <Box mt={3}>
          <CircularProgress />
          <Typography variant="h6" mt={2}>Processing...</Typography>
        </Box>
      )}

      {/* Show Download button when the processing is complete */}
      {!loading && outputFile && (
        <Box mt={3}>
          <Button variant="contained" color="success" onClick={handleDownload}>
            Download Processed File
          </Button>
        </Box>
      )}
    </Box>
  );
}

export default AttendanceList;
