import secrets

import requests

url = "https://webexapis.com/v1/groups"
headers = {"Authorization": secrets.API_KEY}
r = requests.get(url, headers=headers)
r.status_code
print(r.json())
