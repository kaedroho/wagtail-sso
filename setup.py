#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

from wagtail_sso import __version__


setup(
    name='wagtail-sso',
    version=__version__,
    description='',
    author='Karl Hobley',
    author_email='karl@kaed.uk',
    url='https://github.com/kaedroho/wagtail-sso',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[],
    zip_safe=False,
)
