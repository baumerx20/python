import re

def parse_syslogs(log_file_path, pattern):
    try:
        with open(log_file_path, 'r') as file:
            logs = file.readlines()

            for log in logs:
                if re.search(pattern, log):
                    print(log.strip())
    except FileNotFoundError:
        print("Log file not found!")


log_file_path1 = '/var/log/system.log'
pattern1 = r'error|warning'
pattern2 = r'login'

log_file_path2 = '/var/log/messages'
pattern3 = r'error|warning'

log_file_path3 = '/var/log/secure'
pattern4 = r'login'

parse_syslogs(log_file_path1, pattern1)
parse_syslogs(log_file_path1, pattern2)

