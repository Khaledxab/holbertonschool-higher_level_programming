#!/usr/bin/python3
"""err.code2"""
import requests
from sys import argv


def main(argv):
    reqget = requests.get(argv[1])
    if int(reqget.status_code) < 400:
        print(r.text)
    else:
        print("Error code: {}".format(reqget.status_code))


if __name__ == "__main__":
    main(argv)
    