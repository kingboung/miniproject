#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Run as:
#    python LinuxSetup.py build   编译
#    python LinuxSetup.py install 安装（效果同pip install xxx）

from distutils.core import setup
from Cython.Build import cythonize

#cythonize：编译源代码为C或C++，返回一个distutils Extension对象列表
setup(ext_modules=cythonize('version2.pyx'))