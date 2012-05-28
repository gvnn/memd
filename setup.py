#!/usr/bin/env python
from distutils.core import setup

setup(
    name='memd',
    version='0.0.1',
    url='https://github.com/gvnn/memd',
    packages=['memd'],
    install_requires=['python-memcached']
)