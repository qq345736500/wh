import numpy as np
import pandas as pd
import xlrd
import xlwt

data1=xlrd.open_workbook('2/zl2.xls')
table = data1.sheet_by_index(0)


myWorkbook = xlwt.Workbook()
f = myWorkbook.add_sheet('sheet1')
for i in range(table.nrows):
    rnn=table.row(i)[1].value
    svm = table.row(i)[2].value
    labels=table.row(i)[3].value
    if rnn !=svm and rnn==labels:

        f.write(i,0,table.row(i)[0].value)
        f.write(i,1,'1')
        f.write(i,2,'0')

    elif rnn !=svm and svm==labels:

        f.write(i,0,table.row(i)[0].value)
        f.write(i, 1,'0')
        f.write(i, 2,'1')
    elif rnn==svm and svm==labels:
        f.write(i, 0, table.row(i)[0].value)
        f.write(i, 1, '1')
        f.write(i, 2, '1')


myWorkbook.save('shaixuan.xls')

# lstm_col=table.col_values(1)
# label_col=table.col_values(1)
# for i in range(table.nrows):
#     if lstm_col == label_col:
#
#
# LSTM=table.col_values(1)
#
# print(LSTM)



#
# f = open('全對.txt', 'w', encoding='UTF-8')
# sum=0
# for i in range (table.nrows):
#     a=table.row(i)[1].value
#     b=table.row(i)[2].value
#     c=table.row(i)[3].value
#     d=table.row(i)[4].value
#     if a==d and b==d and c==d:
#
#        f.write(table.row(i)[0].value)
#        f.write(table.row(i)[1].value)
#        f.write(table.row(i)[2].value)
#        f.write(table.row(i)[3].value)
#        f.write(table.row(i)[4].value)
#        f.write("\n")
#        sum=sum+1
# f.close()
# print(sum)
#
# import numpy as np
# import pandas as pd
# import xlrd
# import xlwt
#
# data1=xlrd.open_workbook('shaixuan.xls')
# table = data1.sheet_by_index(0)
# f = open('整理篩選.xls', 'w', encoding='UTF-8')
# for i in range(table.nrows):
#
#     if table.row_values(i) != None:
#         f.write(table.row(i)[0].value)
#         f.write(table.row(i)[1].value)
#         f.write(table.row(i)[2].value)
# f.close()
# print("sdsdsdds")