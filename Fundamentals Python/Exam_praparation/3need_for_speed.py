def create_car(model, mileage, fuel):
    return {'name': model, 'mileage': mileage, 'fuel': fuel}


def drive(car, distance, required_fuel):
    if car['fuel'] >= required_fuel:
        car['mileage'] += distance
        car['fuel'] -= required_fuel
        print(f"{car['name']} driven for {distance} kilometers. {required_fuel} liters of fuel consumed.")
        if car['mileage'] >= 100_000:
            print(f"Time to sell the {car['name']}!")
            return True  # if car mileague>= 100k will need to saell the car and remove it from the list below
    else:
        print(f"Not enough fuel to make that ride")
    return False  # if car driven < 100k km - will return false below and will keep using it


def refuel(car, refill_qty):
    max_fuel = 75
    fuel_to_add = min(refill_qty, max_fuel - car['fuel'])
    car['fuel'] += fuel_to_add
    print(f"{car['name']} refueled with {fuel_to_add} liters")


def revert(car, kilometers):
    car['mileage'] -= kilometers
    if car['mileage'] >= 10_000:
        print(f"{car['name']} mileage decreased by {kilometers} kilometers")
    else:
        car['mileage'] = 10_000


def main():
    number_of_cars = int(input())
    cars = []

    for _ in range(number_of_cars):
        car_info = input().split("|")
        car = create_car(car_info[0], int(car_info[1]), int(car_info[2]))
        cars.append(car)
    while True:
        command = input()
        if command == "Stop":
            break
        tokens = command.split(' : ')
        action = tokens[0]
        car_name = tokens[1]
        for car in cars:
            if car['name'] == car_name:
                if action == "Drive":
                    distance = int(tokens[2])
                    fuel = int(tokens[3])
                    if drive(car, distance, fuel):
                        cars.remove(car)
                elif action == "Refuel":
                    refuel_qty = int(tokens[2])
                    refuel(car, refuel_qty)
                elif action == "Revert":
                    kilometers = int(tokens[2])
                    revert(car,kilometers)
    for car in cars:
        print(f"{car['name']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")


main()
