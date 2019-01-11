#  -*- coding: utf-8 -*-
"""
Setuptools script for the overdrive-python project.
"""

import os
from textwrap import fill, dedent
from string import Template
from distutils.core import Command


try:
    from setuptools import setup, find_packages
    from setuptools.command.build_py import build_py
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.build_py import build_py

setup(
    name="anki-overdrive",
    version="0.1.2",
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests",
            "*.ez_setup",
            "*.ez_setup.*",
            "ez_setup.*",
            "ez_setup",
            "*.examples",
            "*.examples.*",
            "examples.*",
            "examples"
        ]
    ),
    py_modules=['overdrive'],
    scripts=[],
    entry_points={},
    include_package_data=True,
    install_requires=['bluepy'],
    zip_safe=False,
    # Metadata for upload to PyPI
    author='Ellis Percival',
    author_email="overdrive_python@failcode.co.uk",
    description=fill(dedent("""\
        Python library for communicating with and controlling the Anki Overdrive
        cars. Forked from https://github.com/xerodotc/overdrive-python/
    """)),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Topic :: Communications",
        "Topic :: System :: Networking"
    ],
    license="MIT",
    keywords="anki overdrive anki-overdrive drive",
    url="https://github.com/flyte/overdrive-python"
)
