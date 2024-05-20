import requests
from bs4 import BeautifulSoup

def fetch_stig_page():
    url = "https://www.stigviewer.com/stig/red_hat_enterprise_linux_8/2023-12-01/MAC-2_Public/"
    try:
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            return response.text
        else:
            print("Failed to fetch page. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

def extract_details(html):
    soup = BeautifulSoup(html, 'html.parser')
    findings = []

    for row in soup.find_all('tr', class_='stig-row'):
        finding = {}
        finding['Severity'] = row.find('td', class_='severity').text.strip()
        finding['Title'] = row.find('td', class_='title').text.strip()
        finding['Description'] = row.find('td', class_='description').text.strip()
        finding['Finding ID'] = row.find('td', class_='fid').text.strip()
        findings.append(finding)

    return findings

def main():
    html = fetch_stig_page()
    print(html)
    if html:
        findings = extract_details(html)
        for finding in findings:
            print("Severity:", finding['Severity'])
            print("Title:", finding['Title'])
            print("Description:", finding['Description'])
            print("Finding ID:", finding['Finding ID'])
            print("=" * 50)

if __name__ == "__main__":
    main()