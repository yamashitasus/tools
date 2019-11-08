#!/usr/bin/env python3
import requests

class reqClass:
    def __init__(self, urls):
        for url in urls:
            res = requests.get(url)
            print(url + " : " + str(res.status_code))

class sie_health:

    urls = ['http:///',
            'http:///',
            'http:///',
            'http:///',
            'http:///',
            'http:///',
            'http:///']

    def __init__(self):
        print("=== XXX HealthCheck Start! ===")

    #def test(self, val):
    #    val = 1111111111
    #    print(self.v)

sie = sie_health()
#req = reqClass(sie.urls)

