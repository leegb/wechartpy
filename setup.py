from setuptools import setup, find_packages
import os

setup(
    name='wechartpy',
    version='2.0',
    description='A Python Interface to WeChart',
    author='ljb_lee',
    author_email='ljb_lee@163.com',
    url='https://github.com/leegb/wechartpy',
    packages=find_packages(),
    install_requires=[
            'wxpy',
            'PyQt5',
    ],

)
