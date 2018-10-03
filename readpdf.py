# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# import sys
# import importlib
# importlib.reload(sys)

# from pdfminer.pdfparser import PDFParser,PDFDocument
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import PDFPageAggregator
# from pdfminer.layout import LTTextBoxHorizontal,LAParams
# from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

# path = r'./static/simple1.pdf'

# def parse():
#   # 以二进制读模式打开
#   fb = open(path, 'rb')
#   # 创建一个pdf文档分析器
#   parser = PDFParser(fb)
#   # 创建一个pdf文档对象
#   doc = PDFDocument()
  
#   parser.set_document(doc)
#   doc.set_parser(parse)

#   doc.initialize("")

#   # pdf 资源管理器
#   resource = PDFResourceManager()

#   # 参数分析器
#   laparam = LAParams()

#   # 聚合器
#   device = PDFPageAggregator(resource, laparams=laparam)

#   # 创建PDF解释器
#   interpreter = PDFPageInterpreter(resource, device)

#   for page in doc.get_pages():
#     # 使用页面解释器来读取
#     interpreter.process_page(page)

#     # 使用聚合器获取内容
#     layout = device.get_result()
    
#     for out in layout:
#       if hasattr(out, "get_text"):
#         print(out.get_text())

  

  