from utils.best_flight import FindBestFlights


def main_menu():
    print('[0] Quit.\n[1] Find cheapest (one leg) flight compared to direct.')


def best_flight_menu():
    while True:
        origin = input('Write origin airport in the "MXP" format: ')

        if origin.isdigit():
            print('Wrong format.')
            continue

        if len(origin) != 3:
            print('Wrong format.')
            continue
        break

    while True:
        destination = input('Write destination airport in the "BER" format: ')

        if destination.isdigit():
            print('Wrong format.')
            continue

        if len(destination) != 3:
            print('Wrong format.')
            continue
        break

    while True:
        date = input('Write desired date in the "YYYY-MM-DD" format: ')

        if date.isdigit():
            print('Wrong format.')
            continue

        if len(date) != 10:
            print('Wrong format.')
            continue
        break

    return origin, destination, date

def main():
    run = True
    while run:
        main_menu()
        selection = input('Select mode to run: ')

        if not selection.isdigit():
            print('Wrong input, only number are accepted.')
            continue

        elif int(selection) == 0:
            run = False
            continue

        elif int(selection) == 1:
            try:
                date = best_flight_menu()
                origin = date[0]
                destination = date[1]
                date = date[2]
                FindBestFlights(origin, destination, date).main()
                continue
            except SystemExit:
                print('[ SHUTTING DOWN ]')


main()
