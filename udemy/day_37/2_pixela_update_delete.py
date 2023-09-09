import requests


USERNAME = "myuser97"
GRAPH_ID = "graph1"
TOKEN = "neiwfni7622ufh8uhqwe"
UPDATE_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20230908"
DELETE_PIXEL_ENDPOINT = UPDATE_PIXEL_ENDPOINT


token_header = {
    "X-USER-TOKEN": TOKEN
}

# update_pixel_parameters = {
#     "quantity": "4.32"
# }
#
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, headers=token_header, json=update_pixel_parameters)
# response.raise_for_status()
# print(str(response.status_code) + " - " + response.text)
# UPDATED YESTERDAY'S PIECE OF DATA
#
# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=token_header)
# response.raise_for_status()
# print(str(response.status_code) + " - " + response.text)
# DELETED AND INSERTED AGAIN
