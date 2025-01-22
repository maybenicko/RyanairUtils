import sys
import time
from utils.header import headers
from utils.routes import get_routes
import requests
import json


class FindBestFlights:
    def __init__(self, origin, destination, date):
        self.origin = origin
        self.destination = destination
        self.date = date
        self.direct_price = 0
        self.route_dict = get_routes()
        self.check_routes = {0: [[self.origin, self.destination]]}
        self.flight_info = []
        self.flight_out = []
        self.flight_in = []

    def builder(self):
        try:
            outs = self.route_dict[self.origin]
            ins = self.route_dict[self.destination]

            for out in outs:
                if out in ins:
                    idx = len(self.check_routes)
                    build = {idx: [[self.origin, out], [out, self.destination]]}
                    self.check_routes.update(build)
            return True
        except KeyError:
            print('[ AIRPORT UNAVAILABLE ]')
            return False

    def checker(self):
        print('[ RETRIEVING FLIGHTS INFO... ]')
        for idx, items in self.check_routes.items():

            for route in items:
                check = False
                if idx == 0:
                    check = True
                data_list = self.get_flight_info(route, check)
                if not data_list:
                    continue
                if items[0] == route:
                    for info in self.flight_info:
                        self.flight_out.append(info)
                elif items[1] == route:
                    for info in self.flight_info:
                        self.flight_in.append(info)
                # need delay as ryanair ip ban easily
                time.sleep(3)

    def get_flight_info(self, route, check):
        try:
            self.flight_info = []
            r = requests.get(
                f'https://www.ryanair.com/api/booking/v4/it-it/availability?ADT=1&TEEN=0&CHD=0&INF=0&Origin={route[0]}&Destination={route[1]}&promoCode=&IncludeConnectingFlights=false&DateOut={self.date}&DateIn=&FlexDaysBeforeOut=2&FlexDaysOut=2&FlexDaysBeforeIn=2&FlexDaysIn=2&RoundTrip=false&ToUs=AGREED',
                headers=headers())

            if 'Availability declined' in r.text:
                print('[ REQUEST DENIED ]')
                print(self.flight_out)
                print(self.flight_in)
                sys.exit()

            trips = r.json()['trips']
            for flight in trips:
                # needed to check for false positive
                date_check = flight['dates']
                for data in date_check:
                    if len(data['flights']) == 0:
                        continue
                    date_out = data['dateOut'].split('T')[0]

                    if date_out != self.date:
                        if check:
                            print('[ NO DIRECT FLIGHTS FOUND ]')
                            sys.exit()
                        continue

                    for data in data['flights']:
                        try:
                            price = int(str(data['regularFare']['fares'][0]['amount']).split('.')[0])
                            if check:
                                self.direct_price = price
                                return False
                        except KeyError:
                            # flight sold out
                            continue
                        time_takeoff = data['segments'][0]['time'][0].split('T')[1].split('.')[0]
                        time_landing = data['segments'][0]['time'][1].split('T')[1].split('.')[0]
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
        except Exception as e:
            print(f'[ ERROR: {e} ]')
            return False

    def found_flights(self):
        print(f'[ DIRECT FLIGHT PRICE: {self.direct_price}€ ]')
        for out_detail in self.flight_out:
            for in_detail in self.flight_in:
                if out_detail['destination'] == in_detail['origin']:

                    # impossible leg
                    if out_detail['time_landing'] > in_detail['time_takeoff']:
                        continue

                    if out_detail['time_landing'].split(':')[0] in ['00', '01', '02']:
                        continue

                    # too expensive
                    total_price = out_detail['price'] + in_detail['price']
                    if total_price > self.direct_price:
                        continue

                    # actual cheaper connections
                    print(f'[ {self.origin} - {out_detail["destination"]} ] [ {out_detail["time_takeoff"]} - {out_detail["time_landing"]} ]')
                    print(f'[ {in_detail["origin"]} - {self.destination} ] [ {in_detail["time_takeoff"]} - {in_detail["time_landing"]} ]')
                    print(f'[ TOTAL PRICE: {total_price}€ ]')

    def main(self):
        if not self.builder():
            return
        self.checker()
        self.found_flights()

