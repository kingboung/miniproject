#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from PIL import Image,ImageFilter,ImageDraw,ImageFont
import random

# 随机字母
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色
def rndColor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 随机颜色
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

# 240 x 60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))

# 创建font对象
font=ImageFont.truetype('C:\\Windows\\winsxs\\x86_microsoft-windows-font-truetype-arial_31bf3856ad364e35_6.1.7601.22739_none_7503c39e24c69a1e\\arial.ttf',36)

# 创建draw对象
draw=ImageDraw.Draw(image)

# 填充每一个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor1())

# 输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())

# 模糊处理
(image.filter(ImageFilter.BLUR)).save('VerifyCode.jpg','jpeg')