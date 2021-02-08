# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in new_theme/__init__.py
from new_theme import __version__ as version

setup(
	name='new_theme',
	version=version,
	description='New Theme',
	author='Theme',
	author_email='a.kuhlani@partner-cons.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
