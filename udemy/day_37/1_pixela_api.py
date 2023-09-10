import requests
import os
import datetime as dt

USERNAME = "myuser97"
GRAPH_ID = "graph1"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"
CREATE_GRAPH_ENDPOINT = f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs"
POST_VALUE_ENDPOINT = f"{CREATE_GRAPH_ENDPOINT}/{GRAPH_ID}"


# create_user_parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=CREATE_USER_ENDPOINT, json=create_user_parameters)
# response.raise_for_status()
# print(str(response.status_code) + " - " + response.text)
# WE HAVE CREATED AN USER


token_header = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# create_graph_parameters = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "ajisai"
# }
#
#
# response = requests.post(url=CREATE_GRAPH_ENDPOINT, headers=token_header, json=create_graph_parameters)
# response.raise_for_status()
# print(response.text)
# WE HAVE CREATED A GRAPH

# We can now add points to the graph:
today = dt.datetime.now().strftime("%Y%m%d")
yesterday = (dt.datetime.today() - dt.timedelta(days=1)).strftime("%Y%m%d")
print(yesterday)


post_value_parameters = {
    "date": yesterday,
    "quantity": "5.32"
}
#
response = requests.post(url=POST_VALUE_ENDPOINT, headers=token_header, json=post_value_parameters)
response.raise_for_status()
print(str(response.status_code) + " - " + response.text)
