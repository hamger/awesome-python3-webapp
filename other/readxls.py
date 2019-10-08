# -*- coding: utf-8 -*-
import xdrlib
import sys
import xlrd
# xlrd 的使用文档 https://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html

permissionFile = './static/permissions.xlsx'

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except ValueError:
        print(str(ValueError))

# 根据名称获取Excel表格中的数据  参数:file：Excel文件路径，by_name：表的名称，col_index：列的索引
def excel_table_byname(file='file.xls', by_name=u'Sheet1', col_index=0):
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    arr = table.col_values(col_index)
    return arr


def getPermission():
    res = excel_table_byname(permissionFile, u'Sheet1', 1)
    permission = []
    for index, item in enumerate(res):
        if index == 0:
            continue
        if item:
            permission.append(item)

    return permission
