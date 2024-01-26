#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays the value of
the variable X-Request-Id in the response header"""

import requests as reqs
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    resp = reqs.get(url)
    print(resp.headers.get('X-Request-Id'))
