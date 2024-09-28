import convertapi
import sys

convertapi.api_credentials = 'secret_dNB0v09AfZ2yOwUe'
file_name = "./Btech_Attendance_2024.pdf"

convertapi.convert('xlsx', {
    'File': file_name
}, from_format = 'pdf').save_files('./')

