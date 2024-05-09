import whois as ws


domain = ws.whois.query('google.com')
print(domain.name)





