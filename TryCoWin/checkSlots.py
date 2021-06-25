import requests
import json
from datetime import date
from datetime import timedelta


class CoWin:
    def __init__(self, loc, today):
        self.pin = loc
        tomorrow = today + timedelta(days=1)
        self.date = tomorrow.strftime("%d-%m-%Y")

    def check_slots(self):
        print(f"Checking vaccination slots on {self.date} at {self.pin}")
        response = requests.get(f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
                                f"pincode={self.pin}&date={self.date}")
        assert response.status_code == 200
        json_cont = json.loads(response.content)
        if json_cont['centers']:
            print("There are Slots Empty in your location.  Please check \"cowin.gov.in\".")
        else:
            print("Sorry!  There is no slot available currently at your location.  Please check later.")


if __name__ == '__main__':
    pin = input("Enter the PIN Code of the area : ")
    check = CoWin(pin, date.today())
    check.check_slots()
