#!/usr/bin/env python

import sys
import os

try:
    from setuptools import setup
    setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

VERSION = "0.0.4"

setup(
    name="python-shorturl",
    version=VERSION,
    description="Python url shortner library for tinyurl.com, is.gd and bit.ly",
    author="Abdul Hamid",
    author_email="ap@appscluster.com",
    url="https://github.com/appscluster/python-shorturl",
    download_url="https://github.com/appscluster/python-shorturl/archive/master.zip",
    packages=["shorturlpy"],
    platforms=['OS Independent'],
    keywords = ['tinyurl', 'shorturl', 'utility', 'bitly', 'is.gd'],
    license='MIT',
    long_description=open("README.md").read(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
    ]
)