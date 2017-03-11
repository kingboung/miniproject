#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 默认端口是5000，访问地址是http://localhost:5000/

from flask import Flask,request,render_template

app=Flask(__name__)


# 首页
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')

# 登录：http://localhost:5000/signin
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('form.html')

# 登录跳转页面：http://localhost:5000/signin
@app.route('/signin',methods=['POST'])
def sign_in():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)

# 运行
if __name__=='__main__':
    app.run(debug=True,use_reloader=False)