import pycountry
import requests as r
import reverse_geocoder as rg


def where_is_the_iss():
    # get lat-lon position of the ISS from the API
    res = r.get("http://api.open-notify.org/iss-now.json")
    obj = res.json()
    lat = obj['iss_position']['latitude']
    lon = obj['iss_position']['longitude']
    coordinates = (lat, lon)

    # run a reverse geocoder search
    results = rg.search(coordinates, verbose=False)
    country_code = results[0]['cc']

    try:
        country_name = pycountry.countries.get(alpha_2=results[0]['cc']).name
    except KeyError:
        country_name = country_code

    message = "The ISS is currently above {city}, {country}".format(
        city=results[0]['name'],
        country=country_name
    )

    print(message)


if __name__ == "__main__":
    where_is_the_iss()
