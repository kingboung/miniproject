#!usr/bin.env python3
# -*- coding:utf-8 -*-
from threading import Thread
import socket,time

# 线程工作
def tcplink(sock,addr):
    print('Accept new connection from %s:%s'%addr)
    sock.send(b'Welcome!')
    while True:
        name=sock.recv(1024)
        if not name or name.decode('utf-8')=='exit':
            break
        time.sleep(1)
        sock.send(('Hello %s'%name.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.'%addr)

# 创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# socket绑定ip与端口（本机，不对外开放）
s.bind(('127.0.0.1',9999))

# 监听端口，最大数量为5
s.listen(5)
print('Waiting connection...')

# 进程通信
while True:
    socket,addr=s.accept()
    thread=Thread(target=tcplink,args=(socket,addr))
    thread.start()
