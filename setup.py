#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="crepo",
    version='0.1.8',
    url="http://github.com/cloudera/crepo/tree/master",
    maintainer="Chad Metcalf",
    maintainer_email="chad@cloudera.com",
    py_modules=['crepo'],
    packages=['crepo'],
    package_dir={'crepo': 'crepo'},
    entry_points = { 'console_scripts': [ 'crepo = crepo.crepo:main', ], },
    install_requires = ['setuptools', 'simplejson'],
)
