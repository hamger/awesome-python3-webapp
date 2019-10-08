# -*- coding: utf-8 -*-
import json
import glob
from readXls import getPermission

fileNames = glob.glob("./static/*.json")
permissions = getPermission()
txt = ''
def write(s):
    global txt
    txt += str(s) + '\n'

def main():
    pagePermission = []
    for index, item in enumerate(fileNames):
        pageName = str(item).split('/').pop().split('--')[0]
        if pageName in permissions:
            pagePermission.append(pageName)
    write('页面权限：')
    write(str(pagePermission))
    write('')
    write('页面内权限：')
    for index, item in enumerate(fileNames):
        pageName = str(item).split('/').pop().split('--')[0]
        write(str(index + 1) + ') ' + item.split('./static/')[1])
        write('-----------------')
        with open(item, 'r') as f:
            jsonStr = str(json.loads(f.read()))
            for point in permissions:
                times = jsonStr.count('window.global.authMap[\'' + point + '\']')
                if (times > 0):
                    write(point + " : " + str(times))
        write('-----------------')
    with open('./result2.txt', 'w') as f:
        f.write(txt)        

if __name__ == "__main__":
    main()
