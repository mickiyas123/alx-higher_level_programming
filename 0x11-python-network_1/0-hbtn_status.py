#!/usr/bin/python3
"""fetches and display body response of https://intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib.request import urlopen

    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("UTF-8")))
