#!/usr/bin/env python3

# Run as:
#    python WindowsSetup.py build_ext --inplace

import sys

sys.path.insert(0, "..")

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

# ext_module = cythonize("TestOMP.pyx")
ext_module = Extension(
    "version3",
    ["version3.pyx"],
    extra_compile_args=["/openmp"],
    extra_link_args=["/openmp"],
)

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(ext_module),
)