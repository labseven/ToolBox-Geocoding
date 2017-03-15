"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import requests
import json
import sys


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_DEMO_API_KEY = "?api_key=wX9NwuHnZU2ToO7GmGR9uw&format=json&"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation" + MBTA_DEMO_API_KEY


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    return requests.get(url).json()


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """

    resp = get_json(GMAPS_BASE_URL + "?address=" + place_name)
    lat = resp["results"][0]["geometry"]["location"]["lat"]
    lng = resp["results"][0]["geometry"]["location"]["lng"]
    return (lat, lng)


def get_nearest_station(latlong):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    resp = get_json(MBTA_BASE_URL + "lat=" + str(latlong[0]) + "&lon=" + str(latlong[1]))
    station_name = resp["stop"][0]["stop_name"]
    dist = resp["stop"][0]["distance"]
    return (station_name, dist)


def find_stop_near(place_name):
    """
    Given a place name or address, print the nearest MBTA stop and the
    distance from the given place to that stop.
    """
    return get_nearest_station(get_lat_long(place_name))

if __name__ == '__main__':
    print(find_stop_near(sys.argv[1]))
