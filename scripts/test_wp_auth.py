import requests
from requests.auth import HTTPBasicAuth

url = "https://juanmoisesdelaserna.es/wp-json/wp/v2/posts"
user = "DoctorenPsicologia"
password = "dp&LVjv3Y%Vbn!C5pu)w)4"

# Try with application password style first
response = requests.get(url, auth=HTTPBasicAuth(user, password))
print(f"Status: {response.status_code}")
if response.status_code == 200:
    print("Auth Success!")
else:
    print(response.text)
