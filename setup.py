#!/usr/bin/env python
import os
from setuptools import setup

from beanstalkc import __version__ as src_version

PKG_VERSION = os.environ.get('BEANSTALKC_PKG_VERSION', src_version)

setup(
    name='beanstalkc_thl',
    version=PKG_VERSION,
    py_modules=['beanstalkc_thl'],

    author='Andreas Bolka',
    author_email='a@bolka.at',
    description='A simple beanstalkd client library',
    long_description='''
beanstalkc_thl is a simple beanstalkd client library for Python. `beanstalkc_thl
<https://github.com/rrguardo/beanstalkc>`_ is a fast, distributed, in-memory
workqueue service.
''',
    url='https://github.com/rrguardo/beanstalkc',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
