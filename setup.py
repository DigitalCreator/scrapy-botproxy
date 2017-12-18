# -*- coding: utf-8 -*
__author__ = '%s%s@botproxy.net' % ('sup', 'port')

from distutils.core import setup

with open('README.md', 'rt') as inp:
    long_description = inp.read()

setup(
    name='scrapy-botproxy',
    version='1.0.0',
    packages=['scrapy_botproxy'],
    url='https://github.com/botproxy/scrapy-botproxy',
    license='MIT',
    author='botproxy',
    author_email='%s%s@botproxy.net' % ('sup', 'port'),
    description=(
        'BotProxy (IP Rotating HTTP proxy) downloader middleware'
        'for Scrapy'),
    long_description=long_description,
    classifiers=[
        'Framework :: Scrapy',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'scrapy>=1.4.0'
    ],
)
