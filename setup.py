#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import media_bundler
import sys

if 'sdist' in sys.argv:
    import mmf_release_tools
    version = mmf_release_tools.generate_release_version(media_bundler.__version__, __file__)
    mmf_release_tools.write_release_version(version)
else:
    with open("RELEASE-VERSION", "r") as f:
        version = f.readlines()[0].strip()

setup(
    name='django-media-bundler',
    version=version,
    author='Reid Kleckner',
    author_email='rnk@mit.edu',
    description="Django application that bundles your Javascript/CSS, "
               +"and sprites your icons.",
    packages=find_packages(),
    zip_safe=False,
    url='http://github.com/rnk/django-media-bundler/',
    classifiers=[
        "Environment :: Web Environment",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    long_description="",
)
