#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': '{}'.format(email)}
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("UTF-8"))
