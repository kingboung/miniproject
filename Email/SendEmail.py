#!usr/bin/env python3
# -*- coding:utf-8 -*-
"""
# 版本一：构造纯文本邮件并发送
from email.mime.text import MIMEText
import smtplib

# 构造纯文本邮件
msg=MIMEText('Hello,send by Python...','plain','utf-8')

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server=input('SMTP server:')

# 发送邮件
server=smtplib.SMTP(smtp_server,25)# SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""
"""
# 版本二：完整的邮件（含收发件人、主题）
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr(Header(name,'utf-8').encode(),addr)

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server=input('SMTP server:')

# 构造邮件
msg=MIMEText('Hello,send by Python...','plain','utf-8')
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()
# 发送邮件
server=smtplib.SMTP(smtp_server,25)# SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""
"""
# 版本三：HTML邮件
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr(Header(name,'utf-8').encode(),addr)

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server=input('SMTP server:')

# 构造邮件
msg=MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>', 'html', 'utf-8')
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()

# 发送邮件
server=smtplib.SMTP(smtp_server,25)# SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""
"""
# 版本四：发送附件
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib
import base64

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr(Header(name,'utf-8').encode(),addr)

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server=input('SMTP server:')

# 邮件对象
msg=MIMEMultipart()
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()

msg.attach(MIMEText('Send with file...','plain','utf-8'))

# 天假附件就是加上一个MIMEBase，从本地读取一个图片
with open ('test.jpg','rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型：
    mime=MIMEBase('image','jpeg',filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    mime=base64.b64encode(mime)
    # 天假到MIMEMultipart
    msg.attach(mime)

# 发送邮件
server=smtplib.SMTP(smtp_server,25)# SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""
"""
# 版本五：图片嵌入邮件正文
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib
import base64

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr(Header(name,'utf-8').encode(),addr)

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server=input('SMTP server:')

# 邮件对象
msg=MIMEMultipart()
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()

msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

# 天假附件就是加上一个MIMEBase，从本地读取一个图片
with open ('test.jpg','rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型：
    mime=MIMEBase('image','jpeg',filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    mime=base64.b64encode(mime)
    # 天假到MIMEMultipart
    msg.attach(mime)

# 发送邮件
server=smtplib.SMTP(smtp_server,25)# SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""
"""
# 版本六：同时支持plain和HTML
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr

import smtplib
import base64

def _format_addr(s):
    name,addr=parseaddr(s)
    return formataddr(Header(name,'utf-8').encode(),addr)

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server=input('SMTP server:')

# 邮件对象
msg=MIMEMultipart('alternative')
msg['From']=_format_addr('Python爱好者<%s>'%from_addr)
msg['To']=_format_addr('管理员<%s>'%to_addr)
msg['Subject']=Header('来自SMTP的问候......','utf-8').encode()

msg.attach(MIMEText('hello','plain','utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8'))

# 天假附件就是加上一个MIMEBase，从本地读取一个图片
with open ('test.jpg','rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型：
    mime=MIMEBase('image','jpeg',filename='test.jpg')
    # 加上必要的头信息
    mime.add_header('Content-Disposition','attachment',filename='test.png')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码
    mime=base64.b64encode(mime)
    # 天假到MIMEMultipart
    msg.attach(mime)

# 发送邮件
server=smtplib.SMTP(smtp_server,25)# SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""
"""
# 版本七：加密SMTP
from email.mime.text import MIMEText
import smtplib

# 构造纯文本邮件
msg=MIMEText('Hello,send by Python...','plain','utf-8')

# 输入Email地址和口令：
from_addr=input('From:')
password=input('Password:')

# 输入收件人地址
to_addr=input('To:')

# 输入SMTP服务器地址
smtp_server='smtp.gmail.com

# 发送邮件
smtp_port=587
server=smtplib.SMTP(smtp_server,smtp_port)# SMTP协议的默认端口是25
server.starttls()
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
"""""