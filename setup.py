from setuptools import find_packages, setup

VERSION = '0.1.1'
DESCRIPTION = 'Python library to help faster upload of data into Neo4J'

classifiers_list = [
    "Development Status :: 1 - Planning",
    "Intend Audience :: Developers",
    "Programming Language :: Python :: 3",
    "Programming Language :: Neo4j's Cypher :: 4.4",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows :: Windows 10",
]

setup(
    name='enopython',
    packages=find_packages(include=['neopython']),
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    author='Gabriel Henrique Alencar Medeiros and Ramiz Hagverdiyev',
    author_email='<henrique382@gmail.com>',
    license='MIT',
    keywords=['python','neo4j','knowledge graph','ontology', 'big data'],
    install_requires=[
        'atomicwrites==1.4.0',
        'attrs==21.4.0',
        'bleach==5.0.0',
        'certifi==2021.10.8',
        'cffi==1.15.0',
        'charset-normalizer==2.0.12',
        'commonmark==0.9.1',
        'cryptography==37.0.2',
        'docutils==0.18.1',
        'idna==3.3',
        'importlib-metadata==4.11.3',
        'jeepney==0.8.0',
        'keyring==23.5.0',
        'more-itertools==8.13.0',
        'neo4j==4.4.3',
        'pkginfo==1.8.2',
        'pluggy==1.0.0',
        'py==1.11.0',
        'pycparser==2.21',
        'Pygments==2.12.0',
        'pytest==4.4.1',
        'pytest-runner==4.4',
        'pytz==2022.1',
        'readme-renderer==35.0',
        'requests==2.27.1',
        'requests-toolbelt==0.9.1',
        'rfc3986==2.0.0',
        'rich==12.4.1',
        'SecretStorage==3.3.2',
        'six==1.16.0',
        'tqdm==4.64.0',
        'twine==4.0.0',
        'urllib3==1.26.9',
        'webencodings==0.5.1',
        'zipp==3.8.0'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=classifiers_list,
)

