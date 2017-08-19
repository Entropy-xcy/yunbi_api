from __future__ import print_function
import json
import requests
import matplotlib.pyplot as plt

'''
Get available markets
'''


def get_markets():
    url = 'https://yunbi.com//api/v2/markets.json'
    html = requests.get(url)
    raw_json = html.text
    json_object = json.loads(raw_json)
    markets = []
    for i in json_object:
        markets.append(i['id'])
    return markets

if __name__ == '__main__':
    for i in get_markets():
        print(i)
