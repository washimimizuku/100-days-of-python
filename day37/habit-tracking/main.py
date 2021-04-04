from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()


PIXELA_TOKEN = os.environ.get('PIXELA_TOKEN')
PIXELA_USERNAME = os.environ.get('PIXELA_USERNAME')
PIXELA_URL = "https://pixe.la/v1/users"
PIXELA_GRAPH = "graph1"

authentication_headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Create User
user_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=PIXELA_URL, json=user_parameters)
print(response.text)

# Create Graph
graph_parameters = {
    "id": PIXELA_GRAPH,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
response = requests.post(url=f"{PIXELA_URL}/{PIXELA_USERNAME}/graphs", json=graph_parameters, headers=authentication_headers)
print(response.text)

# Create Pixel
today = datetime.now() # Alternative: today = datetime(year=2021, month=4, day=4)
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.74"
}
response = requests.post(url=f"{PIXELA_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH}", json=pixel_parameters, headers=authentication_headers)
print(response.text)

# Update Pixel
pixel_parameters = {
    "quantity": "4.5"
}
response = requests.put(url=f"{PIXELA_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH}/{today.strftime('%Y%m%d')}", json=pixel_parameters, headers=authentication_headers)
print(response.text)

# Delete Pixel
response = requests.delete(url=f"{PIXELA_URL}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH}/{today.strftime('%Y%m%d')}", headers=authentication_headers)
print(response.text)
