# shodanscan

usage: shodanscan.py [-h] [-f FILE] -a API [--single SINGLE] [-q QUERY]
                     [-o OUTFILE]

Search a list of IP addresses across Shodan.io using the restful api output in json


| Examples | Result |
| -------- | ------ |
| `./shodanscan.py -a api.txt -f ips.txt` | Runs a shodan search for every ip in 'ips.txt' |
| `./shodanscan.py -a api.txt --single 1.1.1.1` | Runs a shodan search for the single ip address '1.1.1.1' |
| `./shodanscan.py -a api.txt -q 'apache country:US'` | Runs a raw query against shodan for anything after '-q' |
| `./shodanscan.py -a api.txt -f ips.txt -d` | Runs a reverse dns search on every ip in 'ips.txt' |
| `./shodanscan.py -a api.txt -d domain.com` | Runs a subdomain query for 'domain.com' |
