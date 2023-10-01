#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using the requests package.
"""

import requests

if __name__ == "__main__":
    url = requests.get('https://alx-intranet.hbtn.io/status')
    response = url.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(response), response))
