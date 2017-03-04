#!usr/bin/env python3
# -*- coding:utf-8 -*-
import hashlib

db={}

def register(username,password):
    if username in db:
        print('该用户已经注册！1')
        return 0
    md5=hashlib.md5()
    md5.update((password+username).encode('utf-8'))
    md5_right=md5.hexdigest()
    db[username]=md5_right

def login(username,password):
    if username not in db:
        print('不存在该用户')
        return 0
    md5_right=db[username]
    md5_enter=hashlib.md5()
    md5_enter.update((password+username).encode('utf-8'))
    md5_verify=md5_enter.hexdigest()
    if md5_verify==md5_right:
        print('登陆成功！')
    else:
        print('登录失败：密码错误！')

if __name__=='__main__':
    while(True):
        print("注册：1；登录：2")
        code=int(input())
        if code==1:
            username=input('用户名：')
            password=input('密码：')
            register(username,password)
        elif code==2:
            username=input('用户名：')
            password=input('密码：')
            login(username,password)
        elif code==3:
            print(db)
        else:
            print('输入指令出错！')
