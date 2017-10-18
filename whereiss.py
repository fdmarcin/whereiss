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

    message = "The ISS is currently above " + results[0]['name'] + ", " + \
    results[0]['cc'] + "."

    print(message)


if __name__ == "__main__":
    where_is_the_iss()
