#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pyjn",
    version="0.0.1",
    author="Arghadeep Chaudhury,Siddhartha Bhattacharya",
    author_email="arghadeep.chaudhury@gmail.com,siddhartha.bhattacharya@in.ibm.com",
    description="JSON Ref Resolver for standard JSON Schema with Max and Min Schema Generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepstartup/pyjn",
    packages=find_packages(),
    install_requires=['flatten_json'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)