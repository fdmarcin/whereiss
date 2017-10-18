==============================
Where in the world is the ISS?
==============================

A python tool to check where the ISS is and return the country/area below it.

What it will do:

1. Check the location of the ISS by using the `ISS API <http://open-notify.org/Open-Notify-API/ISS-Location-Now/>`_.
2. Map the long-lat to a country (`reverse-geocode <https://pypi.python.org/pypi/reverse_geocode/>`_ or `reverse geocoder <https://github.com/thampiman/reverse-geocoder>`_).
3. Print out a sentence like "The ISS is currently above <place>".
