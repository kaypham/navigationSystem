#Kelly Pham 25384246. Project 3

import json
import urllib.parse
import urllib.request

APPKEY = "Fmjtd%7Cluu8216znd%2Cal%3Do5-9425uf"
Base_MapRequest_URL = "http://open.mapquestapi.com/directions/v2"
Base_ElevationRequest_URL = "http://open.mapquestapi.com/elevation/v1"

def decode_the_map(url: str) -> 'json':
    response = None
    try:
        url = urllib.parse.unquote(url)
        response = urllib.request.urlopen(url)
        data = response.read()
        str_data = data.decode(encoding = 'utf-8')
        return json.loads(str_data)
    finally:
        if response != None:
            response.close()

def build_search_URL(journey: list) -> 'url':
    query_parameters = [('from', journey[0])]
    for each in journey[1:]:
        destination = ('to', each)
        query_parameters.append(destination)
    return Base_MapRequest_URL + '/route?key=' + APPKEY + "&" + urllib.parse.urlencode(query_parameters)

def build_elevation_URL(url: str) -> str:
    parsed_url = decode_the_map(url)
    list_of_url = []
    for location in parsed_url['route']['locations']:
        query_parameters = [('unit', 'f')]
        latlong = ''
        latlong += '{:.4f},{:.4f},'.format(location['latLng']['lat'], location['latLng']['lng'])
        latlongcollection = ('latLngCollection', latlong[:-1])
        query_parameters.append(latlongcollection)
        list_of_url.append(Base_ElevationRequest_URL + '/profile?key=' + APPKEY + "&" + urllib.parse.urlencode(query_parameters))
    return list_of_url



