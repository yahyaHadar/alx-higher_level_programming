#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

import urllib.request as urlreq
import urllib.parse as urlpar
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {
        'email': email,
    }
    encoded_data = urlpar.urlencode(values).encode('ascii')
    req = urlreq.Request(url, data=encoded_data)
    with urlreq.urlopen(req) as resp:
        cont = resp.read().decode('utf-8')
        print(f"{cont}")
