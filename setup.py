# coding: utf-8

"""
    Hostinger API Python SDK

    API Version: 0.0.20

    NOTE: This file is auto-generated, DO NOT EDIT THIS FILE MANUALLY!
    If you want to contribute or request a new feature, please create an issue or pull request on https://github.com/hostinger/api
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

def read(filename):
    return open(filename).read()

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "hostinger_api"
VERSION = "0.0.10"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Hostinger API",
    author="Hostinger",
    author_email="devs@hostinger.com",
    url="https://github.com/hostinger/api-python-sdk",
    keywords=["hostinger", "openapi", "python", "sdk", "rest", "api"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="MIT",
    long_description_content_type='text/markdown',
    long_description=(read('README.md')),
    package_data={"hostinger_api": ["py.typed"]},
)