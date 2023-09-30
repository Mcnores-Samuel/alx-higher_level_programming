#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers['X-Request-Id'])
