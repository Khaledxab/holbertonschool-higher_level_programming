#!/usr/bin/python3
"""commits fetcher"""
import requests
from sys import argv


def commits():
    repos_name = argv[1]
    owner_name = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner_name, repos_name)
    r = requests.get(url)
    data = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(data[i].get("sha"), data[i].get(
                "commit").get("author").get("name")))
    except:
        pass


if __name__ == "__main__":
    commits()
