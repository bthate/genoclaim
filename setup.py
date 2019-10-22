#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# GENOCLAIM - genocide claim to the dutch governent.

""" setup.py """

import os
import sys

if sys.version_info.major < 3:
    print("you need to run GENOCLAIM with python3")
    os._exit(1)

try:
    use_setuptools()
except:
    pass

try:
    from setuptools import setup
except Exception as ex:
    print(str(ex))
    os._exit(1)

with open('README') as file:
    long_description = file.read()

setup(
    name='genoclaim',
    version='12',
    url='https://bitbucket.org/bthate/genoclaim',
    author='Bart Thate',
    author_email='bthate@dds.nl',
    description=" EM_T04_OTP-CR-117_19 - genocide claim to the King of the Netherlands. - een wettelijk voorschrift voor het toedienen van medicatie waarvan men weet dat het gif betreft.",
    long_description=long_description,
    license='MIT',
    include_package_data=True,
    zip_safe=False,
    install_requires=["obot"],
    scripts=["bin/genoclaim"],
    packages=["genoclaim"],
    data_files=[("", ["README"])],
    classifiers=['Development Status :: 3 - Alpha',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: Unix',
                 'Programming Language :: Python',
                 'Topic :: Utilities'
                ]
)
