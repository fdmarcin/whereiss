import requests as r


res = r.get("http://api.open-notify.org/iss-now.json")
obj = res.json()


def mainfunc():
    lat = obj['iss_position']['latitude']
    lon = obj['iss_position']['longitude']
    pass

if __name__ == "__main__":
    mainfunc()


# import urllib2
# import json

# req = urllib2.Request("http://api.open-notify.org/iss-now.json")
# response = urllib2.urlopen(req)

# obj = json.loads(response.read())

# print obj['timestamp']
# print obj['iss_position']['latitude'], obj['data']['iss_position']['latitude']

# # Example prints:
# #   1364795862
# #   -47.36999493 151.738540034
