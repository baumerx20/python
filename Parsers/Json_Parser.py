import json
import re
import numpy as np

my_file = "/Users/dix/Python/python/Parsers/webserver_log.json"
message = "Error"

with open(my_file, "r") as read_file:
    file = json.load(read_file)
    count = 0
    for data in file:
        match = re.search(message, data['message'])
        if match:
            count = count+1
            print(data, count)

        
        
