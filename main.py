# GDYNIA = Location(float(54,5189), float(18,5319))

# Repetetive functions

def try_float(message):
    input_check = False
    while not input_check:
        try:
            user_input = float(input(f"{message}").replace(",","."))
            return user_input
        except ValueError:
            print("Błąd. Spróbuj ponownie")

# Base Code

from datetime import datetime, timedelta

available_locations = {}

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
    print(f"Dostępne lokacje: {available_locations}")
    location_name = input("Podaj nazwę miasta: ").upper()
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
    

#RUN APP
latitude, longitude = select_location()
date = get_date()
print(date)
print(available_locations)
