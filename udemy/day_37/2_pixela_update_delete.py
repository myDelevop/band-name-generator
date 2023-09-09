import requests


USERNAME = "myuser97"
GRAPH_ID = "graph1"
TOKEN = "neiwfni7622ufh8uhqwe"
UPDATE_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20230908"

token_header = {
    "X-USER-TOKEN": TOKEN
}

update_pixel_parameters = {
    "quantity": "4.32"
}

response = requests.put(url=UPDATE_PIXEL_ENDPOINT, headers=token_header, json=update_pixel_parameters)
response.raise_for_status()
print(str(response.status_code) + " - " + response.text)
