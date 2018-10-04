#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

from urllib import request as req
from http import cookiejar

url = "http://www.baidu.com"
print("第一种方法")
response1 = req.urlopen(url)
print(response1.getcode())
print(len(response1.read()))

print("第二种方法")
request=req.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2=req.urlopen(request)
print(response2.getcode())
print (len(response2.read()))


print("第三种方法")
cj=cookiejar.CookieJar()
opener=req.build_opener(req.HTTPCookieProcessor(cj))
req.install_opener(opener)
response3=req.urlopen(url)
print(response3.getcode())
print(cj)
print(response3.read())