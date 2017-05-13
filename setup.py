#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='tweet_cloud',
    version='0.1.0',
    description="Sandbox for Twitter API and cloud databases",
    long_description=readme + '\n\n' + history,
    author="Craig Corcoran",
    author_email='ccor5588@gmail.com',
    url='https://github.com/craig-corcoran/tweet_cloud',
    packages=[
        'tweet_cloud',
    ],
    package_dir={'tweet_cloud':
                 'tweet_cloud'},
    entry_points={
        'console_scripts': [
            'tweet_cloud=tweet_cloud.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD license",
    zip_safe=False,
    keywords='tweet_cloud',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
