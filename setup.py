#! /usr/bin/env python

import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.version_info >= (3, 0):
       package_dir = {'': 'py3'+os.sep+'src'}
else:
       package_dir = {'': 'py2'+os.sep+'src'}

setup(name="python-irclib",
      version="0.4.8",
      py_modules=["irclib", "ircbot"],
      package_dir=package_dir,
      author="Joel Rosdahl",
      author_email="joel@rosdahl.net",
      url="http://python-irclib.sourceforge.net")
