#!/usr/bin/python3

import re
from setuptools import setup, find_packages


def find_version():
    with open('mwtab/__init__.py', 'r') as fd:
        version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                            fd.read(), re.MULTILINE).group(1)
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

REQUIRES = [
    "docopt >= 0.6.2",
    "jsonpickle >= 0.9.5",
    "matplotlib >= 2.1.1",
    "numpy >= 1.14.0",
    "SAGA-optimize >= 1.0.1",
    "scipy >= 1.1.0"
]

setup(

    name='moiety_modeling',
    version=find_version(),
    packages=find_packages(),
    license="The Clear BSD License",
    author_email="hji236@g.uky.edu",
    description="",
    keywords="",
    install_requires=REQUIRES,
    url="",
    long_description=open('README.rst').read(),
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: The Clear BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],


)