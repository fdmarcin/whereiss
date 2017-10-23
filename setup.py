from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='whereiss',

    version='0.1',

    description='A python tool to check where the ISS is and return the area/country below it.',

    long_description=long_description,

    url='https://github.com/fdmarcin/whereiss',
    download_url='https://github.com/fdmarcin/whereiss/archive/0.1.tar.gz',

    author='Marcin Sędłak-Jakubowski',
    author_email='fdmarcin@gmail.com',

    license='MIT',

    install_requires=['pycountry', 'requests', 'reverse_geocoder'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        # Indicate who your project is intended for
        'Intended Audience :: End Users/Desktop',
        'Topic :: Games/Entertainment',
        'Topic :: Education',
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    entry_points={
        'console_scripts': [
            'whereiss = whereiss:where_is_the_iss'
        ]
    },
)

