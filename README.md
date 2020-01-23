# shodanscan

usage: shodanscan.py [-h] [-f FILE] -a API [--single SINGLE] [-q QUERY]
                     [-o OUTFILE]

Search a list of IP addresses across Shodan.io using the restful api output in json


Examples:

`./shodanscan.py -a api.txt -f ips.txt -o out.txt`

`./shodanscan.py -a api.txt -q 'apache country:US'`

`./shodanscan.py -a api.txt -f ips.txt -d`
