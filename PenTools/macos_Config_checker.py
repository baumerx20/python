import subprocess
import os

def check_firewall():
    print("Checking Firewall Status:")
    try:
        firewall_status = subprocess.check_output(['sudo', 'defaults', 'read', '/Library/Preferences/com.apple.alf', 'globalstate']).decode('utf-8').strip()
        if firewall_status == "1":
            print("Firewall is enabled.")
        else:
            print("Firewall is not enabled.")
    except subprocess.CalledProcessError:
        print("Failed to check Firewall status.")

def check_gatekeeper():
    print("Checking Gatekeeper Status:")
    try:
        gatekeeper_status = subprocess.check_output(['sudo', 'spctl', '--status']).decode('utf-8').strip()
        if gatekeeper_status == "assessments enabled":
            print("Gatekeeper is enabled.")
        else:
            print("Gatekeeper is not enabled.")
    except subprocess.CalledProcessError:
        print("Failed to check Gatekeeper status.")

def check_sip():
    print("Checking System Integrity Protection (SIP) Status:")
    try:
        sip_status = subprocess.check_output(['csrutil', 'status']).decode('utf-8').strip()
        print("SIP Status:", sip_status)
    except subprocess.CalledProcessError:
        print("Failed to check SIP status.")

def check_secure_boot():
    print("Checking Secure Boot Status:")
    try:
        secure_boot_status = subprocess.check_output(['sudo', 'firmwarepasswd', '--mode', 'getSecureBoot']).decode('utf-8').strip()
        if secure_boot_status == "SecureBoot is enabled.":
            print("Secure Boot is enabled.")
        else:
            print("Secure Boot is not enabled.")
    except subprocess.CalledProcessError:
        print("Failed to check Secure Boot status.")


def check_sensitive_files():
    sensitive_files = [
        '/etc/passwd',
        '/etc/sudoers',
        '/etc/ssh/sshd_config',
        '/private/etc/hosts',
    ]
    print("Checking Sensitive Files:")
    for file_path in sensitive_files:
        print("File:", file_path)
        try:
            permissions = oct(os.stat(file_path).st_mode)[-3:]
            owner = subprocess.check_output(['ls', '-l', file_path]).decode('utf-8').split()[2]
            group = subprocess.check_output(['ls', '-l', file_path]).decode('utf-8').split()[3]
            print("Permissions:", permissions)
            print("Owner:", owner)
            print("Group:", group)
            print("---")
        except Exception as e:
            print("Error:", e)
            print("---")

def check_sensitive_folders():
    sensitive_folders = [
        '/private/tmp',
        '/private/var/tmp',
        '/private/var/db',
        '/private/var/root',
    ]
    print("Checking Sensitive Folders:")
    for folder_path in sensitive_folders:
        print("Folder:", folder_path)
        try:
            permissions = oct(os.stat(folder_path).st_mode)[-3:]
            owner = subprocess.check_output(['ls', '-ld', folder_path]).decode('utf-8').split()[2]
            group = subprocess.check_output(['ls', '-ld', folder_path]).decode('utf-8').split()[3]
            print("Permissions:", permissions)
            print("Owner:", owner)
            print("Group:", group)
            print("---")
        except Exception as e:
            print("Error:", e)
            print("---")

def check_for_vulnerabilities():
    print("Checking for Vulnerabilities:")
    try:
        software_update = subprocess.check_output(['softwareupdate', '--list']).decode('utf-8')
        print(software_update)
    except subprocess.CalledProcessError:
        print("Failed to check for vulnerabilities.")

def check_for_intrusions():
    print("Checking for Intrusions:")
    try:
        failed_logins = subprocess.check_output(['sudo','grep', 'Failed', '/var/log/system.log']).decode('utf-8').strip()
        if failed_logins:
            print("Failed Login Attempts:")
            print(failed_logins)
        else:
            print("No failed login attempts found.")

        suspicious_sudo = subprocess.check_output(['sudo','grep', 'sudo', '/var/log/system.log']).decode('utf-8').strip()
        if suspicious_sudo:
            print("Suspicious Sudo Commands:")
            print(suspicious_sudo)
        else:
            print("No suspicious sudo commands found.")
    except subprocess.CalledProcessError:
        print("Error searching system logs.")

def check_for_malware():
    print("Checking for Malware:")
    try:
        clamscan = subprocess.check_output(['clamscan', '-r', '-v', '/']).decode('utf-8')
        print(clamscan)
    except subprocess.CalledProcessError:
        print("Failed to check for malware.")


def main():
    print("Performing Insecure Configurations Check on macOS...")
    check_firewall()
    check_gatekeeper()
    check_sip()
    check_secure_boot()
    
    print("Performing Insecure Configurations Check on Files and Folders on macOS...")
    check_sensitive_files()
    check_sensitive_folders()

    print("Performing Security Checks on macOS...")
    check_for_vulnerabilities()
    check_for_intrusions()
    check_for_malware()



if __name__ == "__main__":
    main()

