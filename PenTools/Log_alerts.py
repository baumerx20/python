#!/usr/bin/env python3

import os
import re
import time
import smtplib
from email.mime.text import MIMEText
from collections import defaultdict

# TODO Add JSON Config for extensibility
LOG_FILE = "/var/log/auth.log" 
ALERT_THRESHOLD = 5  
CHECK_INTERVAL = 60  
EMAIL_ALERTS = True 
EMAIL_TO = "admin@example.com" 
EMAIL_FROM = "alert@example.com" 
SMTP_SERVER = "smtp.example.com" 

#TODO: Need to evaluate differences in Auth
FAILED_LOGIN_PATTERN = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

failed_attempts = defaultdict(int)

# Internal Set will need integration
def send_email_alert(ip, attempts):
    """Send an email alert."""
    subject = "Security Alert: Multiple Failed Login Attempts Detected"
    body = f"Multiple failed login attempts detected from IP address: {ip}\nNumber of attempts: {attempts}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    with smtplib.SMTP(SMTP_SERVER) as server:
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

def monitor_log():
    with open(LOG_FILE, "r") as file:
        file.seek(0, os.SEEK_END)
        
        while True:
            line = file.readline()
            if not line:
                time.sleep(CHECK_INTERVAL)
                continue
            
            match = FAILED_LOGIN_PATTERN.search(line)
            if match:
                ip_address = match.group(1)
                failed_attempts[ip_address] += 1
                
                if failed_attempts[ip_address] >= ALERT_THRESHOLD:
                    if EMAIL_ALERTS:
                        send_email_alert(ip_address, failed_attempts[ip_address])
                    # Reset the count after alerting
                    failed_attempts[ip_address] = 0

if __name__ == "__main__":
    monitor_log()
Explanation: