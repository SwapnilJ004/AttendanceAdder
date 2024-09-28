import React, { useState, useEffect } from 'react';
import { Box, Typography, List, ListItem, ListItemText } from '@mui/material';
import axios from 'axios';

function AttendanceList() {
  const [attendanceData, setAttendanceData] = useState([]);

  useEffect(() => {
    async function fetchAttendance() {
      try {
        const response = await axios.get('/api/attendance');
        setAttendanceData(response.data);
      } catch (error) {
        alert('Error fetching attendance data');
      }
    }
    fetchAttendance();
  }, []);

  return (
    <Box mt={5}>
      <Typography variant="h4" textAlign="center">Monthly Attendance Records</Typography>
      <List>
        {attendanceData.map((record, index) => (
          <ListItem key={index}>
            <ListItemText primary={`Month: ${record.month}`} secondary={`Total: ${record.total}`} />
          </ListItem>
        ))}
      </List>
    </Box>
  );
}

export default AttendanceList;
