#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: GigantPro
:license: The GPLv3 License (GPLv3)
:copyright: (c) 2023 Xiver organization
"""

with open("pyproject.toml", encoding="utf-8") as file:
    VERSION = file.read().split("=")[2].split('"')[1]

    INSTALL_REQUIRES = [i.strip() for i in file.readlines()]
    INSTALL_REQUIRES = [line for line in INSTALL_REQUIRES[
            INSTALL_REQUIRES.index('[tool.poetry.dependencies]') + 1 :
            INSTALL_REQUIRES.index('[tool.poetry.group.dev.dependencies]')]
        ]

with open("xiver_gpt/README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="xiver_gpt",
    version=VERSION,
    author="GigantPro",
    author_email="gigantpro2000@gmail.ru",
    description=("The module Xiver team use to work with gpt."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xiver/xiver_gpt",
    download_url="https://github.com/xiver/xiver_gpt/archive/master.zip",
    license="The GPLv3 License (GPLv3)",
    packages=["xiver_gpt"],
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
