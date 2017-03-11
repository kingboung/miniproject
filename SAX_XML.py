#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from xml.parsers.expat import ParserCreate
from collections import OrderedDict
import re

class WeatherSaxHandler(object):
    def __init__(self):
        self.__days = ['today', 'tomorrow']
        self.__weather = OrderedDict()
        self.__name = ''        # tag name
        self.__attrs = {}       # tag attributes
        self.__data = ''        # tag text
        self.__today = 0        # date

    def get_weather(self):
        return self.__weather

    def start_element(self, name, attrs):
        self.__name = name
        self.__attrs = attrs

    def end_element(self, name):
        if name == 'pubDate':
            self.__today = int(re.search(r'\d+', self.__data).group(0))
        elif name == 'yweather:location':
            self.__weather['city'] = self.__attrs['city']
            self.__weather['country'] = self.__attrs['country']
        elif name == 'yweather:forecast':
            day = int(re.search(r'\d+', self.__attrs['date']).group(0))
            delta = day - self.__today
            if delta == 0:      # 限定只存今天和明天的数据，防止下表越界
                self.__weather['today'] = OrderedDict()
                self.__weather[self.__days[delta]]['text'] = self.__attrs['text']
                self.__weather[self.__days[delta]]['low'] = int(self.__attrs['low'])
                self.__weather[self.__days[delta]]['high'] = int(self.__attrs['high'])
            if delta == 1:      # 限定只存今天和明天的数据，防止下表越界
                self.__weather['tomorrow'] = OrderedDict()
                self.__weather[self.__days[delta]]['text'] = self.__attrs['text']
                self.__weather[self.__days[delta]]['low'] = int(self.__attrs['low'])
                self.__weather[self.__days[delta]]['high'] = int(self.__attrs['high'])

    def char_data(self, data):
        self.__data = data


def parse_weather(xml):
    parser = ParserCreate()
    handler = WeatherSaxHandler()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    return handler.get_weather()

# 测试:
data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''
weather = parse_weather(data)
assert weather['city'] == 'Beijing', weather['city']
assert weather['country'] == 'China', weather['country']
assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
assert weather['today']['low'] == 20, weather['today']['low']
assert weather['today']['high'] == 33, weather['today']['high']
assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
print('Weather:', str(weather))