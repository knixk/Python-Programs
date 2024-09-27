from urllib.parse import urlparse
import requests
import json

url = "https://facebook.com/hello"
try:
    html = requests.get(url)
except:
    print("error fetching data..")


# print(html.text)
# print(html.json())
print("============")
final_url = urlparse(url).netloc
print(final_url)
# facebook.com



with open('history_data.txt', 'r') as f:
    data = f.readlines()

domain_names = set()

for url in data:
    final_url = urlparse(url).netloc
#     print(final_url)
    final_url = final_url.split(':')[0]
#     print(final_url)
    domain_names.add(final_url)

for item in domain_names:
    print(item)
    
    
import socket
ip_addr = socket.gethostbyname('google.nl')
print(ip_addr)



ip_set = set()

for domain in domain_names:
    try:
        ip_addr = socket.gethostbyname(domain)
        ip_set.add(ip_addr)
    except:
        print(domain)
        
print(ip_set)

