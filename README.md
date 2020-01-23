# shodanscan

usage: shodanscan.py [-h] [-f FILE] -a API [--single SINGLE] [-q QUERY]
                     [-o OUTFILE]

Search a list of IP addresses across Shodan.io using the restful api output in json

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  File containing list of IP addresses to search
  -a API, --api API     API key file
  --single SINGLE       Search a single IP
  -q QUERY, --query QUERY
                        Perform shodan query on string
  -o OUTFILE, --outfile OUTFILE
                        File to write output to


Examples:

`./shodanscan.py -a api.txt -f ips.txt -o out.txt`

`./shodanscan.py -a api.txt -q 'apache country:US'`
