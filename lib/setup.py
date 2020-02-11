#!/usr/bin/env python3

from distutils.core import setup
from pathlib import Path

package_name = 'wit'

assets = [
    "scala-bridge-fetcher_2.12-0.1.0.jar"
]

scripts = [
    'bin/wit',
]

setup(
    name=package_name,
    version='0.1',
    description=(
        "Workspace Integration Tool"
    ),
    author='',
    author_email='',
    url='www.sifive.com',
    packages=[package_name],
    package_data={'': assets},
    long_description=Path('README.md').read_text(),
    scripts=scripts
)
