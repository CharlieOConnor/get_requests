import requests
import json

url_list = [
requests.get("http://www.bbc.co.uk/iplayer"),
requests.get("http://checkip.amazonaws.com"),
requests.get("https://www.bbc.co.uk/missing/thing"),
requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juve nile_Ragdoll.jpg/220px-Juvenile_Ragdoll.jpg"),
requests.get("https://site.mockito.org/")
]

json_data = []

for url in url_list:
    json_data.append({"Url": url.url, "Status-code": url.status_code, "Content-Length": len(url.content)})


print(json.dumps(json_data, indent=2))
