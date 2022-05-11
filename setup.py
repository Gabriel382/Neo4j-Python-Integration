from setuptools import find_packages, setup

setup(
    name='enopython',
    packages=find_packages(include=['neopython']),
    version='0.0.1',
    description='Python library to help faster upload of data into Neo4J',
    author='Gabriel Henrique Alencar Medeiros and Ramiz Hagverdiyev',
    license='MIT',
)

