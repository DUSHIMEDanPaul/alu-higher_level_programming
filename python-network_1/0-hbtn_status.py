#!/usr/bin/python3
"""
This module fetches https://alu-intranet.hbtn.io/status
using the urllib package.
"""

import urllib.request

url = 'http://0.0.0.0:5050/status'

with urllib.request.urlopen(url) as response:
    html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8'))) 

