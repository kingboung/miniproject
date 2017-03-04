#usr/bin/env python3
# -*- coding:utf-8 -*-

from tkinter import *
import threading
import time
import inspect
import ctypes
import json
from urllib import request,parse

# 存储函数的字典
function = {}

# 当前关卡
mission = 0

# 得分
score=0

# url
url='http://localhost:5000/GuessFigure/RESTfulServer'

# 初始化关卡函数字典
function[1] = lambda x: x
function[2] = lambda x: 2 * x
function[3] = lambda x: x ** 2
function[4] = lambda x: x ** 3
function[5] = lambda x: function[3](x) + function[2](x)
function[6] = None

def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


def record(root,result):
    gameWindows=root
    recordWindows = Toplevel(gameWindows)
    recordWindows.title(result)
    size = '%dx%d+%d+%d' % (200, 120, (screenwidth - 200) / 2, (screenheight - 120) / 2)
    recordWindows.geometry(size)

    def postRecord(event=None):
        if(name.get()==''):   return
        global url
        new_url=url+'/LocalScore/records'
        record_data=parse.urlencode([
            ('user_name',name.get()),
            ('user_score',str(score))
        ])
        with request.urlopen(new_url,data=record_data.encode('utf-8')) as f:
            data = f.read()
            data = json.loads(data.decode('utf-8'))
            if data!='OK':  return
        show()

    name = StringVar()
    nameLabel=Label(recordWindows,text='请输入您的名字：')
    nameEntry = Entry(recordWindows, textvariable=name)
    nameEntry.bind('<Return>', postRecord)
    scoreLabel=Label(recordWindows,text='最终得分：'+str(score))

    nameLabel.place(relx=0.3,rely=0.2,anchor=CENTER)
    nameEntry.place(relx=0.5,rely=0.5,anchor=CENTER)
    scoreLabel.place(relx=0.5,rely=0.8,anchor=CENTER)

    def show():
        mainWindows.update()
        mainWindows.deiconify()
        gameWindows.wm_withdraw()
        recordWindows.withdraw()

    recordWindows.protocol("WM_DELETE_WINDOW", show)


def game():
    gameWindows=Toplevel(mainWindows)
    gameWindows.title('游戏中...')
    mainWindows.withdraw()
    size = '%dx%d+%d+%d' % (300, 240, (screenwidth - 300) / 2, (screenheight - 240) / 2)
    gameWindows.geometry(size)

    missionText=StringVar(gameWindows)
    questionText=StringVar(gameWindows)
    answerText=StringVar(gameWindows)
    scoreText=StringVar(gameWindows)
    timeText=IntVar()

    global score
    score=0

    missionLabel=Label(gameWindows,textvariable=missionText)
    questionLabel=Label(gameWindows,textvariable=questionText)
    timeLabel=Label(gameWindows,textvariable=timeText)
    scoreLabel=Label(gameWindows,textvariable=scoreText)
    answerEntry=Entry(gameWindows,textvariable=answerText)

    def missionCount():
        global mission
        mission=mission+1
        global second
        second=10

        if mission==6:
            stop_thread(timeCount)
            mission=0
            gameWindows.withdraw()
            record(gameWindows,'闯关成功')

        else:
            second=10
            missionText.set('关卡 %d' % mission)
            question = '   ' + str(function[mission](1)) + '   ' + str(function[mission](2)) + '   ' + str(
                function[mission](3)) + '   ' + str(function[mission](4)) + '   __'
            questionText.set(question)
            gameWindows.update()

    def count():
        global second
        while True:
            timeText.set(second)
            time.sleep(1)
            second=second-1
            if second==0:
                missionCount()
                answerText.set('')
                second=10

    def answerDone(event=None):
        global score
        global mission
        if answerText.get()==str(function[mission](5)):
            score+=mission*second
            scoreText.set('得分:'+str(score))
            missionCount()
            answerText.set('')
        else:
            stop_thread(timeCount)
            mission = 0
            gameWindows.withdraw()
            record(gameWindows, '闯关失败')

    scoreText.set('得分:'+str(score))

    missionLabel.place(relx=0.5,rely=0.1,anchor=CENTER)
    questionLabel.place(relx=0.5,rely=0.3,anchor=CENTER)
    timeLabel.place(relx=0.8,rely=0.1,anchor=CENTER)
    answerEntry.place(relx=0.5,rely=0.6,anchor=CENTER)
    scoreLabel.place(relx=0.5,rely=0.8,anchor=CENTER)
    answerEntry.bind('<Return>', answerDone)

    missionCount()

    timeCount = threading.Thread(target=count)
    timeCount.start()

    def show():
        global mission
        global flag
        mainWindows.update()
        mainWindows.deiconify()
        gameWindows.withdraw()

        mission=0
        stop_thread(timeCount)

    gameWindows.protocol("WM_DELETE_WINDOW", show)


def rank(extend_url):
    rankWindows=Toplevel(mainWindows)
    rankWindows.title('排行榜')
    mainWindows.withdraw()
    size = '%dx%d+%d+%d' % (300, 240, (screenwidth - 300) / 2, (screenheight - 240) / 2)
    rankWindows.geometry(size)

    def getRank():

        def fillItem(score,name):
            length=len(score)
            multiLength=28-length
            return ' '*12+score+' '*multiLength+name

        global url
        new_url=url+extend_url
        with request.urlopen(new_url) as f:
            data = f.read()
            data = json.loads(data.decode('utf-8'))
            if(f.status!=200):  return
            length=len(data)
            for i in range(length):
                rankListbox.insert(i+1,fillItem(str(data[i]['user_score']),data[i]['user_name']))


    nameLabel=Label(rankWindows,text='名字')
    scoreLabel=Label(rankWindows,text='分数')
    rankListbox=Listbox(rankWindows,selectmode = EXTENDED)
    scrollTopDown=Scrollbar(rankWindows)
    #scrollLeftRight=Scrollbar(rankWindows,orient='horizontal')

    thread=threading.Thread(target=getRank)
    thread.start()

    rankListbox.configure(yscrollcommand=scrollTopDown.set)
    #rankListbox.configure(xscrollcommand=scrollLeftRight.set)
    scrollTopDown['command'] = rankListbox.yview
    #scrollLeftRight['command'] = rankListbox.xview

    nameLabel.grid(row=0,column=10,columnspan=5)
    scoreLabel.grid(row=0,column=3,columnspan=3)
    rankListbox.grid(row=1,column=0,columnspan=20,ipadx=70,ipady=16)
    scrollTopDown.grid(row=0,column=20,rowspan=2,ipady=83,sticky='s')
    #scrollLeftRight.grid(row=2,column=0,columnspan=20,ipadx=70)

    def show():
        mainWindows.update()
        mainWindows.deiconify()
        rankWindows.withdraw()

    rankWindows.protocol("WM_DELETE_WINDOW", show)

mainWindows=Tk()
mainWindows.title('猜数字')
screenwidth = mainWindows.winfo_screenwidth()
screenheight = mainWindows.winfo_screenheight()
size = '%dx%d+%d+%d' % (300, 240, (screenwidth - 300)/2, (screenheight - 240)/2)
mainWindows.geometry(size)
playBtn=Button(mainWindows,text='开始游戏',command=game)
playBtn.place(relx=0.5, rely=0.3, anchor=CENTER)
rankAllBtn=Button(mainWindows,text='总排行榜',command=lambda:rank('/AllScore/rank'))
rankAllBtn.place(relx=0.5,rely=0.7,anchor=CENTER)
rankLocalBtn=Button(mainWindows,text='本地排行榜',command=lambda:rank('/LocalScore/rank'))
rankLocalBtn.place(relx=0.5,rely=0.5,anchor=CENTER)
mainWindows.mainloop()
