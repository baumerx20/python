import json

json_file_path = 'large_data.json'  # Update with your JSON file path

def parse_json(json_file_path, chunk_size=1000):
    with open(json_file_path, 'r') as json_file:
        parser = json.parse(json_file)
        buffer = []
        for prefix, event, value in parser:
            if event == 'start_map' and len(buffer) >= chunk_size:
                yield buffer
                buffer = []
            buffer.append((prefix, value))
        if buffer:
            yield buffer


for chunk in parse_json(json_file_path):
    for prefix, value in chunk:
        print(prefix, value)