import whois as ws
import argparse


domain = ws.whois.query('google.com')
print(domain.name)





