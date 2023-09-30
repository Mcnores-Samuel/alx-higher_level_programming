#!/usr/bin/python3
"""Fetches a URL and displays the body of the response (decoded in utf-8)."""
if __name__ == "__main__":
    import urllib.request
    import urllib

    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
