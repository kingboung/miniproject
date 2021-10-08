#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import timeit

lon1,lat1,lon2,lat2=-72.345,34.323,-61.823,54.826
num=500000 #调用50万次

t=timeit.Timer("v1.great_circle(%f,%f,%f,%f)"%(lon1,lat1,lon2,lat2),
               "import version1 as v1")
print('纯python版本用时:'+str(t.timeit(num))+'sec')

t=timeit.Timer("v2.great_circle(%f,%f,%f,%f)"%(lon1,lat1,lon2,lat2),
               "import version2 as v2")
print('python+c版本用时:'+str(t.timeit(num))+'sec')

t=timeit.Timer("v3.great_circle(%f,%f,%f,%f)"%(lon1,lat1,lon2,lat2),
               "import version3 as v3")
print('纯c版本用时:'+str(t.timeit(num))+'sec')