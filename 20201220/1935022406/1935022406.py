import xlrd
def read_excel():
    data = xlrd.open_workbook(r"D:\testdat\testdat\studentsmsg.xlsx")
    #table = data.sheet_by_name('Sheet1')#通过名称获取
    sheet = data.sheet_by_index(0)#通过索引顺序获取
    nrows = sheet.nrows
    ncols = sheet.ncols
   # print(table.name, table.nrows, table.ncols)
    for row in range(1,nrows):
        row_values = sheet.row_values(row,0,4)
        name = row_values[0]
        number = row_values[1]
        position = row_values[2]
        print(name,number,position,"\n")
read_excel()
