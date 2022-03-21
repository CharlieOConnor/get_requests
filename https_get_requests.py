import requests
import json

class get_requests:
    def create_url_list():
        url_list = [
                    requests.get("http://www.bbc.co.uk/iplayer"),
                    requests.get("http://checkip.amazonaws.com"),
                    requests.get("https://www.bbc.co.uk/missing/thing"),
                    requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Juve nile_Ragdoll.jpg/220px-Juvenile_Ragdoll.jpg"),
                    requests.get("https://site.mockito.org/")
                    ]
        return url_list

    def create_json_data():           
        json_data = []
        temp_url_list = get_requests.create_url_list()
        for url in temp_url_list:
            json_data.append({"Url": url.url, "Status-code": url.status_code, "Content-Length": len(url.content)})
        return json_data

print(json.dumps(get_requests.create_json_data(), indent=2))
