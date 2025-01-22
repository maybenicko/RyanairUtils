import requests


def get_routes():
    route_dict = {}

    # get all active routes
    r = requests.get('https://www.ryanair.com/api/views/locate/3/airports/it/active').json()
    for item in r:
        route_list = []
        route_fix = item['routes']
        for x in route_fix:
            if 'airport' in x:
                route_list.append(x.split(':')[1])
        origin = item['iataCode']
        _ = {origin: route_list}
        route_dict.update(_)

    return route_dict
