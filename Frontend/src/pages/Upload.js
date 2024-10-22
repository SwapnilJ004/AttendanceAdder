import React, { useState } from 'react';
import { Box, Button, Typography, TextField, CircularProgress } from '@mui/material';
import axios from 'axios';

function Upload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [success, setSuccess] = useState(false);
  const [processing, setProcessing] = useState(false);
  const [downloadLink, setDownloadLink] = useState('');

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert('Please select a file first');
      return;
    }

    const formData = new FormData();
    formData.append('file', selectedFile);

    setProcessing(true); // Start processing animation

    try {
      const response = await axios.post('http://127.0.0.1:5000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      if (response.data.new_filename) {
        setSuccess(true);
        console.log("File uploaded, starting to poll for processing...");
        pollForProcessedFile(response.data.new_filename); // Pass the filename for tracking
      } else {
        alert('File uploaded but processing failed. Response: ' + JSON.stringify(response.data));
        setProcessing(false); // Stop animation on failure
      }
    } catch (error) {
      alert('Error uploading file: ' + error.message);
      setProcessing(false); // Stop animation on failure
    }
  };

  const pollForProcessedFile = async () => {
    const intervalId = setInterval(async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/latest-processed-file`);
        console.log("Polling response:", response.data); // Debugging log
  
        if (response.data.output_file) {
          clearInterval(intervalId);
          setDownloadLink(response.data.output_file); // Store the output filename
          setProcessing(false); // Stop processing animation
        }
      } catch (error) {
        console.error('Error checking processed file:', error);
      }
    }, 20000); // Check every 20 seconds
  };  

  return (
    <Box mt={5} textAlign="center">
      <Typography variant="h4">Upload Attendance</Typography>
      <Box mt={3}>
        <TextField type="file" onChange={handleFileChange} />
        <Button variant="contained" color="primary" onClick={handleUpload} sx={{ ml: 2 }}>
          Upload
        </Button>
      </Box>
      <Typography variant="h6" mt={3}>
        Upload a .jpg or a .png image file for calculating its sum.
      </Typography>
      {success && (
        <Box mt={3}>
          <Typography variant="h6" color="green">✔ File processed successfully! Loading...</Typography>
        </Box>
      )}
      {processing && (
        <Box mt={3}>
          <CircularProgress />
          Processing ...
        </Box>
      )}
      {!processing && downloadLink && (
        <Box mt={3}>
          <Typography variant="h6">Processing Complete! </Typography>
          <Button variant="contained" color="primary" href={`http://127.0.0.1:5000/api/output/${downloadLink}`} download>
            Download CSV
          </Button>
        </Box>
      )}
    </Box>
  );
}

export default Upload;
