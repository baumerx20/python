import json
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message", help="python message file path")
parser.add_argument("my_file", help="python message file path")
args = parser.parse_args()

#print(args.domain)

#my_file = "/Users/dix/Python/python/Parsers/webserver_log.json"
#message = "Error"

with open(args.my_file, "r") as read_file:
    file = json.load(read_file)
    count = 0
    for data in file:
        match = re.search(args.message, data['message'])
        if match:
            count = count+1
            print(data, count)

        
        
