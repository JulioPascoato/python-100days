import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "jpascoato"
TOKEN = "juliopascoato2022"

user_params = {
    "token": "juliopascoato2022",
    "username": "jpascoato",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
graph_id = "graph1"

pixel_endpoint = f"{graph_endpoint}/{graph_id}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "100"

}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
