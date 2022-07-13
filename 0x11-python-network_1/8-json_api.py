#!/usr/bin/python3
"""Search API"""
import requests
from sys import argv


def api():
    if len(argv) > 1:
        a = argv[1]
    else:
        """no arg"""
        a = ""
    value = {"q": a}
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, value)
    try:
        json_data = r.json()
        if json_data == {}:
            """json is empty"""
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except:
        print("Not a valid JSON")


if __name__ == "__main__":
    api()
