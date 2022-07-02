#!/usr/bin/python3
"""a Python script"""
import urllib.request
import sys


def fetcher():
    with urllib.request.urlopen(sys.argv[1]) as reply:
        print(reply.getheader('X-Request-Id'))


if __name__ == "__main__":
    fetcher()
