import json
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt

#Log Parser that will pull from source and display as a visual
#TODO Set up the integration

def read_json_log(file_path):
    with open(file_path, 'r') as file:
        logs = json.load(file)
    return logs

def count_error_occurrences(logs, error_type):
    error_count = 0
    error_dates = []
    error_details = []

    for log in logs:
        if log.get('error') == error_type:
            error_count += 1
            error_dates.append(log.get('date'))
            error_details.append(log)

    return error_count, error_dates, error_details

def count_errors_by_year(error_dates):
    year_count = defaultdict(int)
    for date in error_dates:
        year = datetime.strptime(date, "%Y-%m-%d").year
        year_count[year] += 1
    return year_count

def analyze_other_logs(logs, error_type):
    other_logs = [log for log in logs if log.get('error') != error_type]
    log_types = defaultdict(int)
    
    for log in other_logs:
        log_types[log.get('error')] += 1

    return log_types

def create_graph(error_count, year_count, log_types):
    years = list(year_count.keys())
    error_counts_by_year = list(year_count.values())
    
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    axs[0].bar(years, error_counts_by_year, color='blue')
    axs[0].set_title('Error Occurrences by Year')
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Count')

    log_types_keys = list(log_types.keys())
    log_types_values = list(log_types.values())
    axs[1].pie(log_types_values, labels=log_types_keys, autopct='%1.1f%%', startangle=140)
    axs[1].set_title('Other Log Data Distribution')

    plt.tight_layout()
    plt.show()

def main():
    file_path = 'path_to_your_log_file.json'
    error_type = 'specific_error'  # Replace with the specific error type you're looking for

    logs = read_json_log(file_path)
    error_count, error_dates, error_details = count_error_occurrences(logs, error_type)
    year_count = count_errors_by_year(error_dates)
    log_types = analyze_other_logs(logs, error_type)
    
    print(f"Error '{error_type}' found {error_count} times.")
    print(f"Dates of occurrences: {error_dates}")
    print(f"Error details: {error_details}")
    print(f"Error occurrences by year: {year_count}")
    print(f"Other log data: {log_types}")

    create_graph(error_count, year_count, log_types)

if __name__ == "__main__":
    main()