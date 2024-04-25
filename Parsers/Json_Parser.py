import json

# Path to your JSON log file
json_log_file_path = "your_log_file.json"

# Define the application error you want to search for
error_to_find = "Application Error"

# Open and read the JSON log file
try:
    with open(json_log_file_path, "r") as file:
        log_data = json.load(file)
except FileNotFoundError:
    print("Log file not found. Please provide the correct path to the JSON log file.")
    exit()
except json.JSONDecodeError:
    print("Invalid JSON format. Please check your JSON log file.")
    exit()

# Search for the application error in the log data
error_count = 0
for entry in log_data:
    if "message" in entry and error_to_find in entry["message"]:
        print(f"Error found at timestamp {entry['timestamp']}: {entry['message']}")
        error_count += 1

if error_count == 0:
    print(f"No '{error_to_find}' found in the log file.")
else:
    print(f"Total {error_count} occurrences of '{error_to_find}' found in the log file.")