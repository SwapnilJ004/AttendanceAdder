// src/components/Footer.js
import React from 'react';
import { Box, Typography } from '@mui/material';

function Footer() {
  return (
    <Box 
      component="footer" 
      sx={{ py: 2, textAlign: 'center', bgcolor: '#f1f1f1', mt: 'auto' }}
    >
      <Typography variant="body2" color="textSecondary">
        © 2024 Attendance Adder
      </Typography>
    </Box>
  );
}

export default Footer;
