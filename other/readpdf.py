#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

# 你需要在当前文件的目录下运行改文件
path = '../static/Tuesdays_with_Morrie.pdf'


def parse():
    # 以二进制读模式打开
    fb = open(path, 'rb')
    # 创建一个pdf文档分析器
    parser = PDFParser(fb)
    # 创建一个pdf文档对象
    doc = PDFDocument()

    # 连接分析器与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize("")

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # pdf 资源管理器，来管理共享资源
        resource = PDFResourceManager()
        # 参数分析器
        laparam = LAParams()
        # 聚合器
        device = PDFPageAggregator(resource, laparams=laparam)
        # 创建PDF解释器
        interpreter = PDFPageInterpreter(resource, device)

        # 循环遍历列表，每次处理一个page的内容 
        for page in doc.get_pages(): # doc.get_pages() 获取page列表
            # 使用页面解释器来读取
            interpreter.process_page(page)
            # 使用聚合器获取内容
            layout = device.get_result()

            for out in layout:
                if hasattr(out, "get_text"):
                    print(out.get_text())

if __name__ == '__main__':
    parse()
