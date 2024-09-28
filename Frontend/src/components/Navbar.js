import React from 'react';
import { AppBar, Toolbar, Typography, Button } from '@mui/material';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Attendance Adder
        </Typography>
        <Button color="inherit" component={Link} to="/">Home</Button>
        <Button color="inherit" component={Link} to="/upload">Upload</Button>
        <Button color="inherit" component={Link} to="/attendance">Attendance</Button>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
