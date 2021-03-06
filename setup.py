#!/bin/env python
# -*- coding: utf-8 -*-

"""Setup.py for the GWtool Python package."""


# Package version:
version='0.0.0'

# Get long description from README.md:
with open('README.md', 'r') as fh:
    long_description = fh.read()

# Set package properties:
from setuptools import setup
setup(
    name='gwtool',
    description='Simple tools for working with gravitational waves.',
    author='Marc van der Sluys',
    url='https://github.com/MarcvdSluys/GWtool',
    
    packages=['gwtool'],
    install_requires=['numpy'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    
    version=version,
    license='EUPL 1.2',
    keywords=['gravitational waves','astronomy','physics'],
    
    # See: https://pypi.org/pypi?:action=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
    ]
)
