#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response.
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    try:
        with requests.get(url) as response:
            response.raise_for_status()
            print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
