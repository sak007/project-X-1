from setuptools import setup, find_packages

setup(
    name='ProjectName',
    version='0.1',
    description='Project Description',
    author='CSC510 - Group 32',
    author_email='rjain25@ncsu.edu',
    packages=find_packages(),
    tests_require=['pytest'],
    classifiers=[
        "License :: OSI Approved :: Apache License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Topic :: Project Name",
    ],

    license='Apache',
    install_requires=[
        'pytest',
    ]
)