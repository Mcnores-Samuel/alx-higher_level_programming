#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "http://89ec69ad7361.6aa4e383.alx-cod.online:5000/search_user"
    try:
        q = {"q": sys.argv[1]}
    except IndexError:
        q = {"q": ''}
    response = requests.post(url, q)
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data['id'], data['name']))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
