# Repetetive functions

def try_float(message):
    input_check = False
    while not input_check:
        try:
            user_input = float(input(f"{message}").replace(",","."))
            return user_input
        except ValueError:
            print("Błąd. Spróbuj ponownie")

def print_available_locations():
    location_name_list = []
    for location_name, data in available_locations.items():
        location_name_list.append(location_name)
    print(f"Dostępne lokacje: {location_name_list}")


# Base Code

import requests
import json
from datetime import datetime, timedelta

available_locations = {
    "GDYNIA": {
        "latitude": 54.5189,
        "longitude": 18.5319
    }
}

TODAY = datetime.now().date()
TOMORROW = TODAY + timedelta(days=1)

def add_new_city(location_name):
    location_latitude = try_float("Podaj szerokość geograficzną: ")
    location_longitude = try_float("Podaj długość geograficzną: ")
    available_locations[location_name] = {
        "latitude": location_latitude,
        "longitude": location_longitude
    }

def select_location():
    print_available_locations()
    location_name = None
    while not location_name:
        location_name = input("Podaj nazwę miasta: ").upper()
        if len(location_name) == 0:
            print("Błąd. Spróbuj ponownie")
            location_name = None
    if location_name not in available_locations:
        print("Nie wykryto miasta.")
        add_new_city(location_name)
    latitude = available_locations[location_name].get("latitude")
    longitude = available_locations[location_name].get("longitude")
    return latitude, longitude
    

def get_date():
    date_correct = False
    while not date_correct:
        global TODAY, TOMORROW
        print(f"Podaj date (YYYY-MM-DD). Pozostaw pole puste, aby wyświetlić dla jutra, tj.: {TOMORROW}")
        date = input(": ")
        if len(date) == 0:
            return TOMORROW
        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            return date
        except ValueError:
            print("Niepoprawny format daty.\n Spróbuj ponownie")

def get_api_data(url, user_latitude, user_longitude, user_date):
    api_data = requests.get(url.format(latitude = user_latitude, longitude = user_longitude, searched_date = user_date))
    if api_data.status_code == 200:
        api_data = json.loads(api_data.text)
        return api_data
    else:
        print("Bład wczytywania danych.")
        return False
    
def get_rain_data(api_data):
    if not api_data:
        pass
    else:
        rain_sum = api_data["daily"].get("rain_sum")[0]
        try:
            rain_sum = float(rain_sum)
            if rain_sum > 0:
                print("Będzie padać")
            elif rain_sum == 0:
                print("Nie będzie padać")
            else:
                print("Nie wiem")
        except ValueError:
            print("Nie wiem")
    

#RUN APP
latitude, longitude = select_location()
searched_date = get_date()
URL = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=rain&daily=rain_sum&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}"
api_data =  get_api_data(URL, latitude, longitude, searched_date)
get_rain_data(api_data)

