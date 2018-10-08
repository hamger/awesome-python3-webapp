#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import urllib.request as req
from http import cookiejar
import re
from bs4 import BeautifulSoup as bs

resp = req.urlopen(
    "https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = bs(resp, "html.parser")
urls = soup.find_all('a', href=re.compile(r'^/wiki/'))
for url in urls:
    if not re.search(r'\.(jpg|png|JPG|PNG)$', url["href"]):
        print(url.get_text() + '-->' + url["href"])
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='test',
                                     charset='utf8mb4')
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建一条sql语句
                sql = "insert into `urls` (`urlname`, `urlhref`) values(%s, %s)"
                # 执行sql语句
                cursor.execute(
                    sql, (url.get_text(), 'https://en.wikipedia.org' + url["href"]))
                # 提交
                connection.commit()    
        finally:
            connection.close()
