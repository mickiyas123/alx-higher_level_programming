#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and
displays the body of the response"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from urllib.error import HTTPError
    import sys

    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode("UTF-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
