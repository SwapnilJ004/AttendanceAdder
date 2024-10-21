import React, { useState } from 'react';
import { Box, Button, Typography, TextField, CircularProgress } from '@mui/material';
import { useNavigate } from 'react-router-dom';  // Import useNavigate for redirect
import axios from 'axios';

function Upload() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [success, setSuccess] = useState(false);  // New state for success tick animation
  const navigate = useNavigate();  // Use for redirecting

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
  
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
  
      if (response.data.output_file) {
        setSuccess(true); // Show success tick animation
  
        // Delay the redirect to show the success message
        setTimeout(() => {
          navigate('/attendance'); // Redirect to Attendance page after success
        }, 3000); // 3-second delay
      } else {
        alert('File uploaded but processing failed.');
      }
    } catch (error) {
      alert('Error uploading file: ' + error.message);
    }
  };
  
  

  return (
    <Box mt={5} textAlign="center">
      <Typography variant="h4">Upload Attendance</Typography>
      
      {/* File input and upload button */}
      <Box mt={3}>
        <TextField type="file" onChange={handleFileChange} />
        <Button variant="contained" color="primary" onClick={handleUpload} sx={{ ml: 2 }}>
          Upload
        </Button>
      </Box>
      
      <Typography variant="h6" mt={3}>
        Upload a .jpg or a .png image file for calculating its sum.
      </Typography>

      {/* Show success tick animation */}
      {success && (
      <Box mt={3}>
        <Typography variant="h6" color="green">✔ File uploaded successfully! Switch to Attendance tab to download it.</Typography>
      </Box>
      )}
      </Box>
  )
}
export default Upload;
