#!/usr/bin/env python3
import requests

url = 'http://inet-ip.info'
response = requests.get(url)
print(response.text)
print(response.status_code)
#
#req = urllib.request.Request(url)
#with urllib.requesturlopen(req) as res:
#    body = res.read()
#    print(body)
