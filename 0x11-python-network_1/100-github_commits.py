#!/usr/bin/python3
"""Takes in Github repo nd owner name to list
10 commits (from the most recent to oldest)"""


if __name__ == "__main__":
    import requests
    import sys

    owner = sys.argv[1]
    repo = sys.argv[2]

    response = requests.get(
            "https://api.github.com/repos/{}/{}/commits"
            .format(owner, repo))

    auth_json = response.json()
    count = 0

    for i in auth_json:
        print("{}: {}".format(i["sha"], i["commit"]["author"]["name"]))
        count = count + 1
        if (count == 10):
            break
