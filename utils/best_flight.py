import random
import time

from utils.header import headers
from utils.routes import get_routes
import requests


class FindBestFlights:
    def __init__(self):
        self.origin = 'PSA'
        self.destination = 'BER'
        self.date = '2025-01-26'
        self.route_dict = get_routes()
        self.check_routes = {0: [[self.origin, self.destination]]}
        self.flight_info = []

    def builder(self):
        outs = self.route_dict[self.origin]
        ins = self.route_dict[self.destination]

        for out in outs:
            if out in ins:
                idx = len(self.check_routes)
                build = {idx: [[self.origin, out], [out, self.destination]]}
                self.check_routes.update(build)

    def checker(self):
        list_out = []
        list_in = []

        for idx, items in self.check_routes.items():

            if len(items) == 1:
                print('[ GET PRICE DIRECT FLIGHT... ]')
                continue

            for route in items:
                data_list = self.get_flight_info(route)
                if not data_list:
                    continue
                if items[0] == route:
                    for info in self.flight_info:
                        list_out.append(info)
                elif items[1] == route:
                    for info in self.flight_info:
                        list_in.append(info)
        print(list_out)
        print(list_in)

    def get_flight_info(self, route): # ['XXX', 'YYY']
        try:
            self.flight_info = []
            r = requests.get(
                f'https://www.ryanair.com/api/booking/v4/it-it/availability?ADT=1&TEEN=0&CHD=0&INF=0&Origin={route[0]}&Destination={route[1]}&promoCode=&IncludeConnectingFlights=false&DateOut={self.date}&DateIn=&FlexDaysBeforeOut=2&FlexDaysOut=2&FlexDaysBeforeIn=2&FlexDaysIn=2&RoundTrip=false&ToUs=AGREED',
                headers=headers()).json()
            trips = r['trips']

            for flight in trips:
                # needed to check for false positive
                date_check = flight['dates']
                date_out = ''
                for data in date_check:
                    if len(data['flights']) == 0:
                        continue
                    date_out = data['dateOut'].split('T')[0]

                    if date_out != self.date:
                        continue

                    for data in data['flights']:
                        price = data['regularFare']['fares'][0]['amount']
                        time_takeoff = data['segments'][0]['time'][0].split('T')[1]
                        time_landing = data['segments'][0]['time'][1].split('T')[1]
                        flight_number = data['flightNumber']

                        self.flight_info.append({
                            'origin': route[0],
                            'destination': route[1],
                            'date': date_out,
                            'price': price,
                            'flight_number': flight_number,
                            'time_takeoff': time_takeoff,
                            'time_landing': time_landing
                        })
            if len(self.flight_info) == 0:
                return False
            return True
        except:
            return False


bot = FindBestFlights()
bot.builder()
bot.checker()
