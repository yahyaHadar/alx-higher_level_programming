#!/usr/bin/python3
"""Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id"""

import requests as reqs
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    resp = reqs.get("https://api.github.com/user", auth=auth)
    print(resp.json().get("id"))
