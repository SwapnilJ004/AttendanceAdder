import React, { useState } from 'react';
import { Box, Button, Typography, TextField } from '@mui/material';
import axios from 'axios';

function Upload() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('/api/upload', formData);
      alert('File uploaded successfully!');
    } catch (error) {
      alert('Error uploading file');
    }
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
    </Box>
  );
}

export default Upload;
