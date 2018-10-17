#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

DOC_NAME = 'README.md'

import os
from setuptools import setup, find_packages

long_description = ''

if os.path.isfile(DOC_NAME):
    with open(DOC_NAME) as fp:
        long_description = fp.read()

long_description = long_description or ''

setup(
    long_description=long_description,
    packages=find_packages(),
    # auto generated:
    name='singletonify',
    version='0.2.4',
    description='',
    keywords=['singleton'],
    author='cologler',
    author_email='skyoflw@gmail.com',
    url='https://github.com/Cologler/singletonify-python',
    license='MIT License',
    classifiers=[],
    scripts=[],
    entry_points={},
    zip_safe=False,
    include_package_data=True,
    setup_requires=[],
    install_requires=[],
    tests_require=[],
)
