import subprocess
import os

#System Info
#Operator Handbook MacOS

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


#OS Release
def check_release():
    print("System Release")
    try:
        release_status = subprocess.check_output(['cat','/System/Library/CoreServices/SystemVersion.plist']).decode('utf-8').strip()
        if release_status:
            print("Release Version")
            print(release_status)        
        else:
            print("Cannot find Release")

    except subprocess.CalledProcessError:
        print("Failed to check release.")

#System Software
def check_software():
    print("System Software Version")
    try:
        release_status = subprocess.check_output(['sw_vers','-productVersion']).decode('utf-8').strip()
        if release_status:
            print("Software Version")
            print("MacOS ",release_status)        
        else:
            print("Cannot find Software Version")

    except subprocess.CalledProcessError:
        print("Failed to check software version.")



#Logins
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


#List All Installed Packages
def check_installed():
    print("Current List of Installed apps")
    try:     
        installed_status1 = subprocess.check_output(['ls','-lart','/private/var/db/receipts/']).decode('utf-8').strip()       
        if installed_status1:
            print("Install History")
            print(installed_status1)        
        else:
            print("Cannot find Installed")
    except subprocess.CalledProcessError:
        print("Failed to check Installed.")

#Dump Clipboard
def check_clipboard():
    print("Current Clipboard Contents")
    try:     
        installed_status1 = subprocess.check_output(['pbpaste']).decode('utf-8').strip()       
        if installed_status1:
            print("Clipboard Contents")
            print(installed_status1)        
        else:
            print("Cannot Clipboard Contents")
    except subprocess.CalledProcessError:
        print("Failed to check Cannot Clipboard Contents.")




def main():
    print("Performing Insecure Configurations Check on macOS...")
    check_date()
    check_uname()
    check_hostname()
    check_release()
    check_software()
    check_userlogin()
    check_installed()
    check_clipboard()

if __name__ == "__main__":
    main()