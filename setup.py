#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

def read():
    return open("README.rst", "r").read()

setup(
    name='genoclaim',
    version='30',
    url='https://bitbucket.org/bthate/genoclaim',
    author='B.H.J Thate',
    author_email='bthate@dds.nl',
    description="using the law to administer poison, the king commits genocide - OTP-CR-117/19 - otp.informationdesk@icc-cpi.int",
    long_description=read(),
    long_description_content_type="text/x-rst",
    license='Public Domain',
    zip_safe=False,
    install_requires=["madbot"],
    scripts=["bin/gc"],
    packages=["genoclaim"],
    namespace_packages=["genoclaim"],
    classifiers=['Development Status :: 4 - Beta',
                 'License :: Public Domain',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
