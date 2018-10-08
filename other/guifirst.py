#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter.messagebox as messagebox 

class Application(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.pack()
    self.createWidgets()

  def createWidgets(self):
    self.nameInput = Entry(self)
    # pack()方法把Widget加入到父容器中，并实现布局
    self.nameInput.pack()
    # 当用户点击按钮时，触发hello()，通过self.nameInput.get()获得用户输入的文本后，
    # 使用tkMessageBox.showinfo()可以弹出消息对话框。
    self.alertButton = Button(self, text="hello", command=self.hello)
    self.alertButton.pack()

  def hello(self):
    name = self.nameInput.get() or 'world'
    messagebox.showinfo('message', 'hello, %s' % name)

app = Application()
app.master.title('hello world')
app.mainloop()
