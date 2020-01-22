#!/usr/bin/python3

import requests
import json
import os
import signal
import argparse
import shodan

header = ''' 
███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║
███████╗███████║██║   ██║██║  ██║███████║██╔██╗ ██║███████╗██║     ███████║██╔██╗ ██║
╚════██║██╔══██║██║   ██║██║  ██║██╔══██║██║╚██╗██║╚════██║██║     ██╔══██║██║╚██╗██║
███████║██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║███████║╚██████╗██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
'''

parser = argparse.ArgumentParser(description='Search a list of IP addresses across Shodan.io using the restful api')
parser.add_argument('-f', '--file', help='File containing list of IP addresses to search', required=True)
parser.add_argument('-a', '--api', help='API key file', required=True)
parser.add_argument('-o', '--outfile', help='File to write output to')
args = parser.parse_args()



print(header)
ip_file = open(args.file, "r")
api_file = open(args.api, "r")
SHODAN_API_KEY = api_file.readline().rstrip('\n')
api = shodan.Shodan(SHODAN_API_KEY)

def search():
  for ip in ip_file:
    url = "https://api.shodan.io/shodan/host/" + ip + "?key=" + SHODAN_API_KEY
    request = requests.get(url)
    txt = request.text
    print("\n" + ip )
    parsed = json.loads(txt)
    if args.outfile:
      outfile = open(args.outfile, "w")
      output = json.dumps(parsed, indent=2, sort_keys=True)
      outfile.write(output)
    else:
      print(json.dumps(parsed, indent=2, sort_keys=True))

search()
