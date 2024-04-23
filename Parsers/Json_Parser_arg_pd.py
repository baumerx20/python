import json
import re
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("message", help="python message file path")
parser.add_argument("my_file", help="python message file path")
args = parser.parse_args()

#print(args.domain)

#my_file = "/Users/dix/Python/python/Parsers/webserver_log.json"
#message = "Error"

df = pd.read_json(args.my_file, orient="split", lines=True, chunksize=5)



count = 0
for data in df:
    match = re.search(args.message, data['message'])
    if match:
        count = count+1
        print(data, count)

        
        
