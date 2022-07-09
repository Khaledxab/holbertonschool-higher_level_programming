#!/usr/bin/python3
"""hbtn fetcher"""
import requests


def fetch():
    link = "https://intranet.hbtn.io/status"
    r = requests.get(link)
    r = r.text
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    fetch()
