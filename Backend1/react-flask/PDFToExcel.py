import convertapi
import sys
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

convertapi.api_credentials = 'secret_dNB0v09AfZ2yOwUe'
file_name = "./Temp.pdf"

convertapi.convert('xlsx', {
    # 'File': file_name
    'File': './uploads/Btech_Attendance_2024.pdf'
}, from_format = 'pdf').save_files('./')

