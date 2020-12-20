import csv
import os

#读取学生的信息
with open (r'E:\Python Project\1935021730\testdat\student.csv','r+',encoding='gb18030') as f1:
    lines=csv.reader(f1)
    list1=list(lines)
    
#对文件进行操作（注意:这个文件夹需要放在E:\Python Project目录下才能使用，否则要更换代码中的路径）
    path1=os.path.exists(r'E:\Python Project\1935021730\testdat\101\101.jpg')
    path2=os.path.exists(r'E:\Python Project\1935021730\testdat\102\102.jpg')
    path3=os.path.exists(r'E:\Python Project\1935021730\testdat\103\103.jpg')
    if path1:
        list1[1][2]=r'E:\Python Project\1935021730\testdat\101\101.jpg'
    if path2:
        list1[2][2]=r'E:\Python Project\1935021730\testdat\102\102.jpg'
    if path3:
        list1[3][2]=r'E:\Python Project\1935021730\testdat\103\103.jpg' 
str1=str(list1)

#写入新的csv文件(保存在学号的文件夹中)
with open(r'E:\Python Project\1935021730\student_modify.csv','w',encoding='gb18030',newline="") as f2:
    csv_writer= csv.writer(f2)
    for i in range(4):
        csv_writer.writerow(list1[i])
    
