#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.button=Button(self,text='Alter',command=self.hello)
        self.button.pack()
        '''
        self.label=Label(self,text='Hello world!')
        self.label.pack()
        self.button=Button(self,text='Quit',command=self.quit)
        self.button.pack()
        '''

    def hello(self):
        name=self.nameInput.get()
        messagebox.showinfo('Meaasge','Hello %s'%name)

app=Application()
app.master.title='Hello World'
app.mainloop()