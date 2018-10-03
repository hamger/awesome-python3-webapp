#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request as req
from http import cookiejar
import re
from bs4 import BeautifulSoup as bs

resp = req.urlopen("https://en.wikipedia.org/wiki/Main_Page").read().decode("utf-8")
soup = bs(resp, "html.parser")
urls = soup.find_all('a', href=re.compile(r'^/wiki/'))
for url in urls:
  if not re.search(r'\.(jpg|png|JPG|PNG)$', url["href"]):
    print(url["href"])