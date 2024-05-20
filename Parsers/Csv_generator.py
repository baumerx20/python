import csv
import random
from datetime import datetime, timedelta

# Function to generate a random date between two dates
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Function to generate random severity
def random_severity():
    return random.choice(["High", "Medium", "Low"])

# Function to generate a random finding
def random_finding():
    return "Some Vulnerability " + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))

# Generate CSV file
def generate_csv(filename, rows):
    fieldnames = ["Severity", "Finding", "First Seen", "Last Seen", "Description"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(rows):
            first_seen = random_date(datetime(2020, 1, 1), datetime.now())
            last_seen = random_date(datetime(2020, 1, 1), first_seen)
            writer.writerow({
                "Severity": random_severity(),
                "Finding": random_finding(),
                "First Seen": first_seen.strftime("%Y-%m-%d %H:%M:%S"),
                "Last Seen": last_seen.strftime("%Y-%m-%d %H:%M:%S"),
                "Description": "Some Vulnerability"
            })

if __name__ == "__main__":
    generate_csv("sample_data.csv", 10000)