import os
from http.client import responses

import requests
from datetime import datetime
import pytz

bearer_token = "Bearer WEWAYAWGUMANA"
ph_now = pytz.timezone('Asia/Manila')
date_in_ph = datetime.now(ph_now)
formatted_date = date_in_ph.strftime("%d/%m/%Y")
formatted_time = date_in_ph.strftime("%H:%M:%S")


# NUTRITION KEYS
app_id = os.getenv("APP_ID")
app_keys = os.getenv("APP_KEYS")

sheety_endpoint = "https://api.sheety.co/37890adc0cee5eb428aa2cea7c7aed37/myWorkout/sheet1"
natural_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

description_parameters = {
    "query": input("Tell me what exercise you today: "),
    "weight_kg": input("Input your weight in kg: "),
    "height_cm": input("Input your height in cm: "),
    "age": input("Input your age: ")
}

headers = {
    "x-app-id": app_id,
    "x-app-key": app_keys
}


auth_headers = {
    "Authorization": f"{bearer_token}"
}

# # GET AUTH
# response = requests.post(url=sheety_endpoint, json= headers=auth_headers)
# print(response.text)

#
response_nutrition = requests.post(url=natural_exercise_endpoint, json=description_parameters, headers=headers)
response_nutrition.raise_for_status()
exercise = response_nutrition.json()

# GET REQUEST (SHEETY)
# response = requests.get(url=sheety_endpoint)
# print(response.text)

# CHECK IF ANY ITEMS IN THE LIST
for item in exercise["exercises"]:
    sheets_params = {
        "sheet1" : {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": item["user_input"].title(),
            "duration": item["duration_min"],
            "calories": item["nf_calories"]
    }
    }

    response = requests.post(url=sheety_endpoint, json=sheets_params, headers=auth_headers)
    print(response.text)
