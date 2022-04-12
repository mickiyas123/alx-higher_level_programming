#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password)
   and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    token = sys.argv[2]

    headers = {'Authorization': token}
    response = requests.get(
            "https://api.github.com/users/{}"
            .format(user), headers=headers)
    if response.status_code < 400:
        print(response.json()['id'])
    else:
        print("None")
