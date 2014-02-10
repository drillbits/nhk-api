from setuptools import setup, find_packages

import os
import re

here = os.path.dirname(__file__)


def _get_version(*path):
    try:
        with open(os.path.join(here, *path)) as fp:
            m = re.compile(r".*__version__ = '(.*?)'", re.S).match(fp.read())
            return m.group(1)
    except Exception:
        return '0.0.0'

version = _get_version('src', 'nhk', '__init__.py')


def _read(name):
    try:
        with open(os.path.join(here, name)) as fp:
            return fp.read()
    except Exception:
        return ""

long_description = _read('README.rst')

install_requires = [
    'requests',
]

tests_require = [
]

entry_points = {
    'console_scripts': [
    ],
}

setup(
    name='nhk-api',
    version=version,
    description="Python client for NHK API",
    long_description=long_description,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.3",
    ],
    author='Jiro Nejime',
    author_email='neji@drillbits.jp',
    url='https://github.com/drillbits/nhk-api',
    license='MIT License',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'testing': tests_require,
    },
    test_suite='tests',
    entry_points=entry_points)
