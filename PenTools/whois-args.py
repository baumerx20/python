import whois as ws
import argparse
import pprint
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument("ip", help="python whois.py www.google.com")
args = parser.parse_args()
pprint.pprint(args.ip)

## Has issues with the following format: 2022-04-07T08:53:42.06717+02:00z

def get_whois_info(host):
    whois_info = ws.query(host)
    pprint.pprint(whois_info.__dict__)
    

if __name__ == "__main__":
  get_whois_info(args.ip)
  

