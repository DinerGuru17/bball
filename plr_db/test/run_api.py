from python_yahooapi.yahooapi import *
import json

api = YahooAPI('keydata.txt', 'tokenfile.txt')

json_data = api.request('game/mlb/players').json()

with open('data.txt', 'w') as outfile:
    json.dump(json_data, outfile, sort_keys=True, indent = 4)
