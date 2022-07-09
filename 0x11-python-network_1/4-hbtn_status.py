#!/usr/bin/python3
"""hbtn fetcher"""
from os import link
import requests


def fetch():
    link = "https://intranet.hbtn.io/status"
    r = requests.get(link)
    r = r.text
    print("Body response:")
    print("\t- type: {}".format(type(r)))
    print("\t- content: {}".format(r))


if __name__ == "__main__":
    fetch()
