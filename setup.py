#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-


from setuptools import setup, find_packages


setup(name='otus-project',
      version='1.0',
      url='https://github.com/WolfGung/Otus',
      license='MIT',
      author='Zhukov Pavel',
      author_email='zhukov@otus.ru',
      description='Otus tests project code',
      long_description=open('README.md').read(),
      setup_requires=['pytest>=4.3.1'],
      zip_safe=False)
