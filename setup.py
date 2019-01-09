#!/usr/bin/python3
from setuptools import setup

setup(
    name='RotatingProxyBot',
    version='0.0.3',
    description='A Bot that acts as a Rotating Proxy Crawler, simulating many clients to a single server ',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dgisolfi/RotatingProxyBot',
    author='dgisolfi',
    license='MIT',
    packages=['RotatingProxyBot'],
    install_requires=['requests>=2.19.1','tqdm>=4.28.1'],
    zip_safe=False
)