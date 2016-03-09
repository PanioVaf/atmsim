# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='atmsim',
    version='0.0.1',
    description='Atm Simulator for Exc!te Holidays',
    long_description=readme,
    author='Vafeiadis Panagiotis',
    author_email='pavafeia@gmail.com',
    url='https://github.com/PanioVaf/atmsim',
    license=license,
    packages=find_packages(exclude=('tests'))
)
