import React from 'react';
import { Typography, Box } from '@mui/material';
import homeImage from '../assets/home-image.jpg'; 

function Home() {
  return (
    <Box mt={5} textAlign="center">
      <Typography variant="h3">Welcome to Attendance Adder</Typography>
      <Typography variant="h6" mt={3}>
        Easily upload attendance images and track monthly attendance.
      </Typography>
      
      {/* Image Section */}
      <Box mt={5}>
        <img 
          src={homeImage} 
          alt="Attendance Adder" 
          style={{ 
            width: '70%', 
            maxWidth: '500px', 
            height: 'auto', 
            borderRadius: '8px',
            boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)' 
          }} 
        />
      </Box>
    </Box>
  );
}

export default Home;
