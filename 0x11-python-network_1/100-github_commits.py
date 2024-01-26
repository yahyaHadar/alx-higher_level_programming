#!/usr/bin/python3
""" a Python script that takes 2 arguments
in order to solve this challenge."""

import requests as reqs
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    resp = reqs.get(url)
    commits = resp.json()
    try:
        for i in range(10):
            sha = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except IndexError:
        pass
