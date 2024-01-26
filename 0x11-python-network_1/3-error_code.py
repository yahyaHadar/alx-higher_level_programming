#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and display
the body of the response (decoded in utf-8)."""

import urllib.request as urlreq
import urllib.parse as urlpar
import urllib.error as urlerr
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = urlreq.Request(url)
    try:
        with urlreq.urlopen(req) as resp:
            cont = resp.read().decode('utf-8')
            print(cont)

    except urlerr.HTTPError as e:
        print(f"Error code: {e.code}")
