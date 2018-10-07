#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from urllib import request as req
from urllib.parse import quote

class HtmlDownloader(object):
  def download(self, url):
    if url is None:
      return None
    url_ = quote(url, safe=string.printable)
    response = req.urlopen(url_)
    # response = req.urlopen(url)
    if response.getcode() != 200:
      return None
    
    return response.read()