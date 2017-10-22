from setuptools import setup

setup(
    name='whereiss',

    version='0.1',

    description='A python tool to check where the ISS is and return the area/country below it.',

    url='https://github.com/fdmarcin/whereiss',

    author='fdmarcin',
    author_email='fdmarcin@gmail.com',

    license='MIT',

    install_requires=['requests', 'reverse_geocoder']

)
