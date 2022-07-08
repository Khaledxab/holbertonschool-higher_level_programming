#!/usr/bin/python3
"""POST request"""
from urllib import request
import urllib.parse
from sys import argv


def post():
    url = argv[1]
    values = {"email": argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        Prequest = response.read()
        print(Prequest.decode("utf-8"))


"""execute"""
if __name__ == "__main__":
    post()
