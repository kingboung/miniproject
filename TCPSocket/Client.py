#!usr/bin/env python3
# -*- coding:utf-8 -*-
import socket

# 创建socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 建立连接
s.connect(('127.0.0.1',9999))

# 进程通信
data=s.recv(1024)
print(data.decode('utf-8'))
for name in [b'Jack',b'Mike',b'Rose']:
    s.send(name)
    info=s.recv(1024)
    if info:
        print(info.decode('utf-8'))
    else:
        break

# 关闭socket
s.send(b'exit')
s.close()