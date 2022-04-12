#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
   http://0.0.00.0:5000/search_user with the letter as a parameter
"""


if __name__ == "__main__":
    import requests
    import sys

    q = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q}

    response = requests.post(
            "http://0.0.0.0:5000/search_user",
            data=payload)
    try:
        json_dict = response.json()

        if json_dict == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                    json_dict['id'],
                    json_dict["name"]))
    except ValueError:
        print("Not a valid JSON")
