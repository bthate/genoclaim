#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def read():
    return open("README", "r").read()

setup(
    name='genoclaim',
    version='32',
    url='https://bitbucket.org/bthate/genoclaim',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description="the king commits genocide - OTP-CR-117/19/001 - http://genoclaim.rtfd.io",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license='Public Domain',
    zip_safe=False,
    install_requires=["botlib", "feedparser"],
    scripts=["bin/genoclaim"],
    packages=["genoclaim"],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
