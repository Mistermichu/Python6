# GDYNIA = Location(float(54,5189), float(18,5319))

from datetime import datetime, timedelta

available_locations = []

TODAY = datetime.now().date()
TOMORROW = TODAY + timedelta(days=1)

class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

def add_new_city():
    city_name = input("Podaj nazwę miasta: ").upper
    city_latitude = float(input("Podaj szerokość geograficzną: "))
    city_longitude = float(input("Podaj długość geograficzną: "))
    city_name = city_name.Location(city_latitude, city_longitude)
    available_locations.append(city_name)    

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
print(f"Dostępny lokacje: {available_locations}")
date = get_date()
print(date)
