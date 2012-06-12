#! /usr/bin/env python

import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info >= (3, 0):
       package_dir = {'': 'src3'}
else:
       package_dir = {'': 'src2'}

setup(name="python-irclib",
      version="0.4.8",
      py_modules=["irclib", "ircbot"],
      package_dir=package_dir,
      author="Joel Rosdahl",
      author_email="joel@rosdahl.net",
      url="http://python-irclib.sourceforge.net")
