import subprocess
import os

#System Info
#Operator Handbook

#Date
def check_date():
    print("Current Date")
    try:
        date_status = subprocess.check_output(['date']).decode('utf-8').strip()
        print(date_status)
    except subprocess.CalledProcessError:
        print("Failed to check date.")


#Uname
def check_uname():
    print("System Version of OS")
    try:
        uname_status = subprocess.check_output(['uname','-a']).decode('utf-8').strip()
        print(uname_status)
    except subprocess.CalledProcessError:
        print("Failed to check uname.")

#UHostname
def check_hostname():
    print("System Hostname")
    try:
        hostname_status = subprocess.check_output(['hostname']).decode('utf-8').strip()
        print(hostname_status)
    except subprocess.CalledProcessError:
        print("Failed to check hostname.")


#Linux Release
def check_release():
    print("System Release")
    try:
        release_status = subprocess.check_output(['cat','/proc/version']).decode('utf-8').strip()
        if release_status:
            print("Release Version")
            print(release_status)        
        else:
            print("Cannot find Release")

    except subprocess.CalledProcessError:
        print("Failed to check release.")


def check_userlogin():
    print("Current List of Users Last Login")
    try:
        user_login_status = subprocess.check_output(['last',]).decode('utf-8').strip()
        if user_login_status:
            print("Users Last Login")
            print(user_login_status)        
        else:
            print("Cannot find user logins")

    except subprocess.CalledProcessError:
        print("Failed to check user logins.")






def main():
    print("Performing Insecure Configurations Check on macOS...")
    check_date()
    check_uname()
    check_hostname()
    check_release()
    check_userlogin()

if __name__ == "__main__":
    main()