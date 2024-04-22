import argparse
import socket

parser = argparse.ArgumentParser()
parser.add_argument("domain", help="python nslookup.py www.domain.com")
args = parser.parse_args()
print(args.domain)

class NetworkUtilites:
    def nslookup(self, domain):
        
        nslookup_result_ip = socket.gethostbyname(domain)
        print(nslookup_result_ip)


def run() -> None:
    network_utilities = NetworkUtilites()
    network_utilities.nslookup(args.domain)

run()