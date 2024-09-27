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

