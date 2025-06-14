from setuptools import setup, find_packages

setup(
    name='abdullha',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    author='Abdullha',
    author_email='abdullha@example.com',
    description='A simple greeting package by Abdullha',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/abdullha/abdullha',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
