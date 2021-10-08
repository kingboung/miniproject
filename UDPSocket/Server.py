#!usr/bin.env python3
# -*- coding:utf-8 -*-
import socket

# 创建socket（UDP）
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定ip与port
s.bind(('127.0.0.1',9999))

print('Bind UDP on 9999....')

# 进程通信
while True:
    data,addr=s.recvfrom(1024)
    print('Recieve from %s:%s'%addr)
    s.sendto(('Hello %s'%data.decode('utf-8')).encode('utf-8'),addr)