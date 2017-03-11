#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from html.parser import HTMLParser
from urllib import request
from collections import OrderedDict

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super(MyHTMLParser,self).__init__()
        self.__result=[]#用于控制输出
        self.__node=OrderedDict()
        self.__node['meeting-name']=''
        self.__node['meeting-date']=''
        self.__node['meeting-location']=''
        #handle_starttag与handle_data方法的交互
        self.__nameBool=False
        self.__dateBool=False
        self.__locationBool=False

    #返回扫描结果
    def return_result(self):
        return self.__result

    def handle_starttag(self, tag, attrs):
        if tag=='h3' and attrs[0][1]=='event-title':
            self.__nameBool=True
        if tag=='time' and attrs[0][0]=='datetime':
            self.__dateBool=True
        if tag=='span' and attrs[0][1]=='event-location':
            self.__locationBool=True

    def handle_data(self, data):
        if self.__nameBool:
            self.__node['meeting-name']=data
            self.__nameBool=False
        if self.__dateBool:
            self.__node['meeting-date']=data
            self.__dateBool=False
        if self.__locationBool:
            self.__node['meeting-location']=data
            self.__locationBool=False
            self.__result.append(self.__node)


with request.urlopen('https://www.python.org/events/python-events/') as html:
    content=html.read()
    parser=MyHTMLParser()
    parser.feed(content.decode('utf-8'))
    print(parser.return_result())