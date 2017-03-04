#!\usr\bin\env python3
# -*- coding:utf-8 -*-
def triangles(line):
    L=[]
    x=1
    while x<=line:
        n=x-2
        if x>=3:
            while n>0:
                L[n]=L[n]+L[n-1]
                n=n-1
        L.append(1)
        yield L
        x=x+1
    return 'done'

for x in triangles(10):
    print(x)