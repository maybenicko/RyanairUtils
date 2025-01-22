from utils.header import headers
from utils.routes import get_routes
import requests


class FindBestFlights:
    def __init__(self):
        self.origin = 'PSA'
        self.destination = 'BER'
        self.date = '2025-01-25'
        self.route_dict = get_routes()
        self.check_routes = {0: [self.origin, self.destination]}

    def builder(self):
        outs = self.route_dict[self.origin]
        ins = self.route_dict[self.destination]

        for out in outs:
            if out in ins:
                idx = len(self.check_routes)
                build = {idx: [self.origin, out, self.destination]}
                self.check_routes.update(build)
        print(self.check_routes)

    def checker(self):
        for idx, route in self.check_routes.items():

            while len(route) >= 2:
                print(f'[ {route[0]} - {route[1]} ] [ CHECK FLIGHT... ]')
                route.pop(0)

    def get_direct_price(self):
        r = requests.get(
            f'https://www.ryanair.com/api/booking/v4/it-it/availability?ADT=1&TEEN=0&CHD=0&INF=0&Origin={self.origin}&Destination={self.destination}&promoCode=&IncludeConnectingFlights=false&DateOut={self.date}&DateIn=&FlexDaysBeforeOut=2&FlexDaysOut=2&FlexDaysBeforeIn=2&FlexDaysIn=2&RoundTrip=false&ToUs=AGREED',
            headers=headers()).json()
        trips = r['trips']
        flight_info = self.get_price(trips)

        if len(flight_info) == 0:
            print('No flights found')
            return

        print(f'{flight_info[0]["origin"]} - {flight_info[0]["destination"]}\n')

        for flight in flight_info:
            print(f'{flight["date"]} - {flight["trip_time"]} - {flight["price"]}')

    def get_price(self, trips):
        flight_info = []

        for trip in trips:
            origin_name = trip['originName']
            destination_name = trip['destinationName']
            dates = trip['dates']

            for date in dates:
                date_true = str(date['dateOut']).split('T')[0]
                if self.date != date_true:
                    continue
                flights = date['flights']

                for flight in flights:
                    try:
                        price = flight['regularFare']['fares'][0]['amount']
                        flightkey = flight['flightKey']
                        farekey = flight['regularFare']['fareKey']
                        time_to = str(flight['time'][0]).split('T')[1].split('.')[0]
                        time_l = str(flight['time'][1]).split('T')[1].split('.')[0]
                        flight_number = flight['flightNumber']

                        flight_info.append({
                            'origin': origin_name,
                            'destination': destination_name,
                            'date': date_true,
                            'price': price,
                            'flight_number': flight_number,
                            'trip_time': f'{time_to} - {time_l}',
                            'flightkey': flightkey,
                            'farekey': farekey
                        })
                    except Exception as e:
                        continue
        return flight_info


    def get_indirect(self):
        possible_out = self.route_dict[self.origin]
        possible_in = self.route_dict[self.destination]
        
        print(possible_out)
        print(possible_in)
        
        for middle in possible_out:
            if middle in possible_in:
                print(f'{origin} - {middle} - {destination}')
        
        r = requests.get(
                f'https://www.ryanair.com/api/booking/v4/it-it/availability?ADT=1&TEEN=0&CHD=0&INF=0&Origin={origin}&Destination={destination}&promoCode=&IncludeConnectingFlights=false&DateOut={date}&DateIn=&FlexDaysBeforeOut=2&FlexDaysOut=2&FlexDaysBeforeIn=2&FlexDaysIn=2&RoundTrip=false&ToUs=AGREED',
                headers=headers()).json()

    def main(self):
        self.get_direct_price()


bot = FindBestFlights()
bot.builder()
bot.checker()
