#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import requests

    with requests.get("https://alx-intranet.hbtn.io/status") as response:
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))
