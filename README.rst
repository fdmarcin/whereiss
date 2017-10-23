==============================
Where in the world is the ISS?
==============================

A python tool to check where the ISS is and return the area/country below it.

What it does:

1. Checks the location of the ISS by using the `ISS API <http://open-notify.org/Open-Notify-API/ISS-Location-Now/>`_.
2. Maps the long-lat to a country (using `reverse geocoder <https://github.com/thampiman/reverse-geocoder>`_).
3. Print out a sentence like "The ISS is currently above <place>".

***************
Install and run
***************

To install from PyPI, run:

 ``pip install whereiss``

To install locally, clone or download the repo and run:

 ``pip install -r requirements.txt``

 ``pip install -e .``

************
Requirements
************

* pycountry
* requests
* reverse_geocoder

Works with Python 2.7, and >=3.5

************
Contributing
************

Pull Requests welcome!

Fork the repo, make your changes and submit a Pull Request.
