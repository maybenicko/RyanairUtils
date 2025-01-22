import requests
from src.header import headers


def get_flight_info(origin, destination, date):
    # get all flights for the given route
    r = requests.get(
        f'https://www.ryanair.com/api/booking/v4/it-it/availability?ADT=1&TEEN=0&CHD=0&INF=0&Origin={origin}&Destination={destination}&promoCode=&IncludeConnectingFlights=false&DateOut={date}&DateIn=&FlexDaysBeforeOut=2&FlexDaysOut=2&FlexDaysBeforeIn=2&FlexDaysIn=2&RoundTrip=false&ToUs=AGREED',
        headers=headers()).json()
    trips = r['trips']

    flight_info = []

    # process each trip in the response
    for trip in trips:
        origin = trip['origin']
        origin_name = trip['originName']
        destination = trip['destination']
        destination_name = trip['destinationName']
        dates = trip['dates']

        for date in dates:
            date_true = str(date['dateOut']).split('T')[0]
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
