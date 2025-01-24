from idlelib.rpc import response_queue

import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USERNAME = "amandamendiet"
PIXELA_TOKEN = "kduy74yo3hf4hiwuehweoerqq43yfhh"
USER_PARAMS = {
    'token': PIXELA_TOKEN,
    'username': PIXELA_USERNAME,
    'agreeTermsOfService': "yes",
    'notMinor': "yes",
}
# response = requests.post(url=PIXELA_ENDPOINT, json=USER_PARAMS)
# print(response.text)
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "days",
    "type": "float",
    "color": "ajisai",
}
headers = {
    'X-USER-TOKEN': PIXELA_TOKEN,
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)
POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/graph1"
today = datetime.datetime.today().date().strftime('%Y%m%d')
print(today)
pixel_config = {
    'date':today,
    'quantity':"1"
}
# response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# print(response.text)
UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/graph1/{today}"
update_pixel_config = {
    'quantity':"8"
}
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_config, headers=headers)
# print(response.text)

response = requests.delete(url=UPDATE_PIXEL_ENDPOINT, headers=headers)
print(response.text)
