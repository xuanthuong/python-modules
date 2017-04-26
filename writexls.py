# # xlwt -> only .xls
# # xlsxwriter/openpyxl -> .xlsx
#
# from xlwt import Workbook, Formula, easyxf
#
# wb = Workbook()
# sheet1 = wb.add_sheet('Plan')
# sheet2 = wb.add_sheet('Schedule')
# sheet3 = wb.add_sheet('Resource')
#
# sheet1.write(0, 0, 'This is the plan')
# sheet2.write(0, 1, 'This is the schedule')
# sheet3.write(0, 2, 'This is the resource')
#
# sheet1.col(0).width = 7000
#
# for i in range(10):
#     sheet2.write(i, 0, i)
#
# style1 = easyxf('pattern: pattern solid, fore_colour red;')
# sheet2.write(10, 0, Formula('SUM(A1:A10)'), style1)
#
# wb.save('xlwt_sample.xls')

# from PIL import Image
# import sys
import commands
# usrimg = Image.open(sys.argv[1])
# Converting the image to greyscale.
# captcha = usrimg.convert('1')
# Saving the image as tesseract can read.
# captcha.save('temp.bmp', dpi=(200,200))
# Invoking tesseract from python to extract characters
# commands.getoutput('tesseract D:\WhatsApp.jpeg D:\output')
# Reading the output generated in data.txt
# with open('data.txt', 'r') as data:
#     print data.readline().strip()
