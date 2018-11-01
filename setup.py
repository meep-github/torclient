#!/usr/bin/env python

from distutils.core import setup
from setuptools import *
import os

setup(
    name="torclient",
    version="1.1",
    description="A Simple, Lightweight and Easy To Use, TOR Proxy Library For Python",
    author="petrexxy",
    author_email="psmall.775@gmail.com",
    url="https://github.com/petrexxy",
    packages=["torclient"],
    classifiers=[
              "Programming Language :: Python",
              "Intended Audience :: Penetration Testers/Developers",
              "Topic :: Networking"
    ],
    install_requires=[
              'setuptools',
              'stem',
              'requests',
              'pysocks'
    ]
)
try:
    os.system("cp /torclient/torclient.py /usr/lib/python2.7")
except Exception as e:
    print("Could Not Install!\n")
    print(e)
