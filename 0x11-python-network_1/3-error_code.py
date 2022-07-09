#!/usr/bin/python3
"""err.code"""
from urllib import (request, error)
from sys import argv
from urllib import request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    req0 = argv[1]
    try:
        with urllib.request.urlopen(req0) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
