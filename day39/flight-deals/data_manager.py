import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_FLIGHT_DEALS_API_KEY = os.environ.get('SHEETY_FLIGHT_DEALS_API_KEY')
SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{SHEETY_FLIGHT_DEALS_API_KEY}/flightDeals/prices"
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_FLIGHT_DEALS_API_KEY}",
    "Content-Type": "application/json"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            headers=sheety_headers
        )
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=sheety_headers,
                json=new_data
            )
            print(response.text)
