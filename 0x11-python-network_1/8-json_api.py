#!/usr/bin/python3
""" Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter."""

import requests as reqs
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    json_data = {"q": letter}
    try:
        resp = reqs.post(url, data=json_data)
        js_data = resp.json()
        if js_data == {}:
            print("No result")
        else:
            print(f"[{js_data.get('id')}] {js_data.get('name')}")
    except ValueError:
        print("Not a valid JSON")
