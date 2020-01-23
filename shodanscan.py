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
parser.add_argument('-a', '--api', help='API key file', required=True)
parser.add_argument('-f', '--file', help='File containing list of IP addresses to search')
parser.add_argument('--single', help='Search a single IP')
parser.add_argument('-q', '--query', help='Perform shodan query on string')
parser.add_argument('-d', '--dns', nargs='?', help='Perform shodan dns query on specified domain or reverse dns on IPs in file specified with "-f"')
parser.add_argument('-o', '--outfile', help='File to write output to')
args = parser.parse_args()


def main():
  ip_file=""
  print(header)
  if args.file:
    ip_file = open(args.file, "r")
  api_file = open(args.api, "r")

  if not args.file and not args.single and not args.query and not args.dns:
    parser.print_help()
    exit()

  SHODAN_API_KEY = api_file.readline().rstrip('\n')
  api = shodan.Shodan(SHODAN_API_KEY)
  search(ip_file, SHODAN_API_KEY)



def search(ip_file, SHODAN_API_KEY):
  if args.dns and not args.file:
    domain = args.dns
    url = "https://api.shodan.io/dns/domain/" + domain + "?key=" + SHODAN_API_KEY
    request = requests.get(url)
    txt = request.text
    print("\n" + args.dns)
    parsed = json.loads(txt)
    if args.outfile:
      outfile = open(args.outfile, "w")
      output = json.dumps(parsed, indent=2, sort_keys=True)
      outfile.write(output)
    else:
      print(json.dumps(parsed, indent=2, sort_keys=True))


  if args.query:
    query = args.query
    url = "https://api.shodan.io/shodan/host/search?key=" + SHODAN_API_KEY + "&query=" + query
    request = requests.get(url)
    txt = request.text
    print("\n" + args.query)
    parsed = json.loads(txt)
    if args.outfile:
      outfile = open(args.outfile, "w")
      output = json.dumps(parsed, indent=2, sort_keys=True)
      outfile.write(output)
    else:
      print(json.dumps(parsed, indent=2, sort_keys=True))


  if args.single:
    url = "https://api.shodan.io/shodan/host/" + args.single + "?key=" + SHODAN_API_KEY
    request = requests.get(url)
    txt = request.text
    print("\n" + args.single)
    parsed = json.loads(txt)
    if args.outfile:
      outfile = open(args.outfile, "w")
      output = json.dumps(parsed, indent=2, sort_keys=True)
      outfile.write(output)
    else:
      print(json.dumps(parsed, indent=2, sort_keys=True))


  if args.file and args.dns is None:
    for ip in ip_file:
      url = "https://api.shodan.io/dns/reverse?ips=" + ip + "&key=" + SHODAN_API_KEY
      request = requests.get(url)
      txt = request.text
      print("\n" + ip)
      parsed = json.loads(txt)
      if args.outfile:
        outfile = open(args.outfile, "w")
        output = json.dumps(parsed, indent=2, sort_keys=True)
        outfile.write(output)
      else:
        print(json.dumps(parsed, indent=2, sort_keys=True))

  if args.file and not args.dns:
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

main()
