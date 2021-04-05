from datetime import datetime
import os
import requests
from dotenv import load_dotenv

load_dotenv()


NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')

MY_GENDER = os.environ.get('MY_GENDER')
MY_WEIGHT = os.environ.get('MY_WEIGHT')
MY_HEIGHT = os.environ.get('MY_HEIGHT')
MY_AGE = os.environ.get('MY_AGE')

SHEETY_WORKOUTS_API_KEY = os.environ.get('SHEETY_WORKOUTS_API_KEY')


exercise_query = input("Tell me which exercises you did: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "Content-Type": "application/json"
}
exercise_body = {
    "query": exercise_query,
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}
response = requests.post(
    exercise_endpoint,
    headers=nutritionix_headers,
    json=exercise_body
)
response.raise_for_status()
exercise_data = response.json()

now = datetime.now()
sheety_endpoint = f"https://api.sheety.co/{SHEETY_WORKOUTS_API_KEY}/workoutTracking/workouts"
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_WORKOUTS_API_KEY}",
    "Content-Type": "application/json"
}
for exercise in exercise_data['exercises']:
    sheety_body = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(
        sheety_endpoint,
        headers=sheety_headers,
        json=sheety_body
    )
    response.raise_for_status()
    sheety_data = response.json()
