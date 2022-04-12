#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]

    response = requests.get(
            "https://api.github.com/user",
            auth=(user, token))
    print(response.json().get("id"))
