import requests

from utils.search_flights import get_flight_info
from utils.header import headers


class RetrieveSeats:
    def __init__(self):
        # self.origin = input('Insert origin flight code (ex. "MXP"): ')
        # self.destination = input('Insert destination flight code (ex. "BER"): ')
        # self.date = input('Insert target date of the flight (ex. "YYYY-MM-DD"): ')
        self.s = requests.Session()
        self.useful_flights = []

        self.origin = 'MXP'
        self.destination = "BER"
        self.date = '2025-01-23'

    def get_seats_ind(self):
        for flight in self.useful_flights:
            r = self.s.get(f'https://www.ryanair.com/api/booking/v5/it-it/FareOptions?OutboundFlightKey={flight["flightkey"]}&OutboundFareKey={flight["farekey"]}&AdultsCount=1&ChildrenCount=0&InfantCount=0&TeensCount=0', headers=headers())
            return r

    def uselessmaybe(self):
        print(self.get_seats_ind().text)


    def loop_seats(self):
        flights = get_flight_info(self.origin, self.destination, '2025-01-23')

        if len(flights) == 0:
            print('No flights found.')
            return

        for flight in flights:
            if not flight['date'] == self.date:
                continue
            self.useful_flights.append(flight)

        if len(self.useful_flights) == 0:
            print('No flights found.')
            return
        return

    def main(self):
        self.loop_seats()
        self.uselessmaybe()





bot = RetrieveSeats()
bot.main()
