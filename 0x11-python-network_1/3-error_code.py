#!/usr/bin/python3
"""err.code"""
from urllib import (request, error)
from sys import argv


def errC():
    request0 = request.Request(argv[1]) 
    try:
        with request.urlopen(request0) as response:
            body = response.read()

        print(body.decode('utf8'))
    except error.HTTPerror as e:
        print("error code: {}".format(e.code))


if __name__ == "__main__":
    errC()
