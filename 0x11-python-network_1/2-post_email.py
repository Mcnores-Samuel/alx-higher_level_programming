#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    parsed_data = urllib.parse.urlencode(email)
    parsed_data = parsed_data.encode('ascii')
    req = urllib.request.Request(url, parsed_data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
