import convertapi
import sys
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

convertapi.api_credentials = 'secret_dNB0v09AfZ2yOwUe'
file_name = "./Btech_Attendance_2024"

convertapi.convert('xlsx', {
    'File': file_name + ".pdf"
}, from_format = 'pdf').save_files('./')

