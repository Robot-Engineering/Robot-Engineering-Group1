import os.path as op
import xlrd,xlwt
from xlutils.copy import copy

massage=[]
workbook = xlrd.open_workbook(r'D:\testdat\massage.xlsx')
worksheet = workbook.sheet_by_index(0)
nrows = worksheet.nrows
ncols = worksheet.ncols
print(ncols)
for i in range(nrows):
    a = worksheet.row_values(i, start_colx=0, end_colx=None)
    massage.append(a)
print(massage)
m1 = op.exists(r'D:\testdat\101\101.jpg')
m2 = op.exists(r'D:\testdat\102\102.jpg')
m3 = op.exists(r'D:\testdat\102\102.jpg')

workbooks = xlwt.Workbook(encoding = 'utf-8')
worksheets = workbooks.add_sheet('Sheet1')
for i in range(nrows):
    for j in range(ncols):
        worksheets.write(i,j, label = massage[i][j])
if(m1 == True):
    worksheets.write(1,2,label = 'D:\testdat\101\101.jpg')
if(m2 == True):
    worksheets.write(2,2,label = 'D:\testdat\102\102.jpg')
if(m3 == True):
    worksheets.write(3,2,label = 'D:\testdat\102\102.jpg')
workbooks.save(r'D:\testdat\massage1.xlsx')
