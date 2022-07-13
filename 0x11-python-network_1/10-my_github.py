#!/usr/bin/python3
"""github credentials"""
import requests
from sys import argv

def github()
    session = requests.Session()
    session.auth = (argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=session.auth)
    print(r.json().get('id'))


if __name__ == "__main__":
    github()
