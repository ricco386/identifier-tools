#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This software is licensed as described in the README.rst and LICENSE
# files, which you should have received as part of this distribution.

import os

from setuptools import setup, find_packages
from identifier_tools import __version__ as VERSION

CLASSIFIERS = [
    "Environment :: Console",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Developers",
    "Operating System :: Unix",
    "Operating System :: POSIX :: Linux",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
]


def read_file(name):
    return open(os.path.join(os.path.dirname(__file__), name), encoding="utf-8").read()


setup(
    name="identifier-tools",
    version=VERSION,
    description="Library that helps working with different identifier types.",
    long_description=read_file("README.rst"),
    author="Richard Kellner",
    author_email="richard.kellner@nbs.sk",
    license="MIT",
    url="https://github.com/ricco386/identifier-tools",
    packages=find_packages(),
    install_requires=["postal-codes-tools>1.1.0", "postal-codes-tools<1.2"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    include_package_data=True,
)
