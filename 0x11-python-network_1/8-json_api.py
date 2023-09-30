#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"

    try:
        q = {"q": sys.argv[1]}
    except IndexError:
        q = {"q": ''}
    response = requests.post(url, data=q)
    try:
        response = response.json()
        if response:
            print("[{}] {}".format(response.get("id"), response.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
