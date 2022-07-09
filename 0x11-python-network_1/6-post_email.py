#!/usr/bin/python3
"""POST an email"""
import requests
from sys import argv


def res(argv):
    url = argv[1]
    email = {"email": argv[2]}
    res = requests.post(url, email)
    print(res.text)


if __name__ == "__main__":
    res(argv)
