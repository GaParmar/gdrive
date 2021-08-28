"""
This file packages the src code into a pip package
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='gdrive',  
    version='0.1',
    # scripts=['dokr'] ,
    author="Gaurav Parmar",
    author_email="gauravtparmar@gmail.com",
    description="Google Drive utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaparmar/gdrive",
    packages=["gdrive"],
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
 )