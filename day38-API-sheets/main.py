import requests
from datetime import datetime

APP_ID = "8c28399d"
API_KEY = "c0ea2c348bc5faa45581b347683119b9"

GENDER = "male"
WEIGHT_KG = 100.0
HEIGHT_CM = 170.0
AGE = 40


EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETS_ENDPOINT = "https://api.sheety.co/150aa3f5069fd461144c91794514a6ae/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

exercise_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_parameters, headers=headers)
result = response.json()
# print(result["exercises"])

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%X")

sheet_headers = {
    "Authorization": "Basic anBhc2NvYXRvOkZlcnplcmJtYXoyMDE0"
}
for exercise in result["exercises"]:
    sheet_parameters = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    response = requests.post(url=SHEETS_ENDPOINT, json=sheet_parameters, headers=sheet_headers)
# response.raise_for_status()
# sheet = response.json()


