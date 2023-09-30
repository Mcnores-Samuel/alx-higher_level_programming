#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body
of the response (decoded in utf-8).
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    from urllib.error import HTTPError

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
