import os.path
from setuptools import setup, find_packages

# Get the long description from the relevant file
__here__ = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(__here__, 'README.rst'), 'r') as f:
    long_description = f.read()

setup(
    name='ibflex',
    version='0.1',
    # Note: change 'master' to the tag name when release a new verison
    download_url='https://github.com/csingley/ibflex/tarball/master',

    description=('Parse Interactive Brokers Flex XML reports and convert '
                 'to Python data types'),
    long_description=long_description,

    url='https://github.com/csingley/ibflex',

    author='Christopher Singley',
    author_email='csingley@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords=['Interactive Brokers', 'ibkr', 'flex', 'xml'],

    packages=find_packages(),

    install_requires=['requests'],

    package_data={
        'ibflex': ['README.rst', 'tests/*'],
    },

    entry_points={
        'console_scripts': [
            'flexget=ibflex.client:main',
        ],
    },
)
