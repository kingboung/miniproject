"""
这个版本混搭C和Python
"""

import math

def great_circle(float lon1,float lat1,float lon2,float lat2):
    cdef float radius=3956.0
    cdef float pi=3.14159265
    cdef float x=pi/180.0
    cdef float a,b,theta,c

    a=(90.0-lat1)*(x)
    b=(90.0-lat2)*(x)
    theta=(lon2-lon1)*(x)
    c=math.acos((math.cos(a)*math.cos(b)+math.sin(a)*math.sin(b)*math.cos(theta)))
    return c*radius

'''命令行模式'''
## cython version2.pyx
#  生成一个c文件version2.c

## gcc -c version2.c
#  编译

## gcc -shared version2.o -o version2.pyd
#  把.c文件编译为可导入的使用模块.so(Windows下为.pyd)文件