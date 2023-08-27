import time
from datetime import datetime, timedelta

def get_date():
    print("Podaj date (YYYY-MM-DD).")
    date = input(": ")


today = datetime.now().date()
tomorrow = today + timedelta(days=1)
print(today)
print(tomorrow)