#!/usr/bin/python3

import requests
import json
import os
import signal


file_in = input("IP file: ")
ip_file = open(file_in, "r")
api_file = open("api.txt", "r")
api = api_file.readline().rstrip('\n')

def loop():
  for ip in ip_file:
    url = "https://api.shodan.io/shodan/host/" + ip + "?key=" + api
    request = requests.get(url)
    txt = request.text
    print("\n" + ip )
    parsed = json.loads(txt)
    print(json.dumps(parsed, indent=2, sort_keys=True))

loop()
