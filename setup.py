#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='genoclaim',
    version='26',
    url='https://bitbucket.org/bthate/genoclaim',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description=""" The king admits guilty to genocide - https://genoclaim.rtfd.io - OTP-CR-117/19/001 - otp.informationdesk@icc-cpi.int""",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license='Public Domain',
    zip_safe=True,
    install_requires=["botlib"],
    scripts=["bin/gc"],
    packages=["genoclaim"],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
