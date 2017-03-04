#!usr/bin/env python3
# -*- coding:utf-8 -*-
import socket

# 创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 进程通信
for data in [b'Jack',b'Mike',b'Rose']:
    s.sendto(data,('127.0.0.1',9999))
    print(s.recv(1024).decode('utf-8'))