#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
   http://0.0.00.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            print("No result")
        else:
            response = requests.post(
                    "http://0.0.0.0:5000/search_user",
                    data={'q': sys.argv[1]})
            if response:
                new_dict = response.json()
                print("[{}] {}".format(
                    new_dict['id'],
                    new_dict["name"]))
            else:
                print("Not a valid JSON")
    elif len(sys.argv) == 1:
        print("No result")
