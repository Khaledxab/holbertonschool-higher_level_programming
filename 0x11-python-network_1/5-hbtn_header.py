#!/usr/bin/python3
"""send a request
and display the var X-Request-Id"""
import requests
from sys import argv


def return0(argv):
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))


if __name__ == "__main__":
    return0(argv)
