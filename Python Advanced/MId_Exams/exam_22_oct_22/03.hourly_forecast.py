def forecast(*args):
    locations = {}
    result = ""
    for city, weather in args:
        if weather == "Sunny":
            locations[city] = weather,1
        elif weather == "Cloudy":
            locations[city] = weather,2
        elif weather == "Rainy":
            locations[city] = weather,3
    sorted_locations = sorted(locations.items(),key=lambda x: (x[1][1],x[0]))
    for location, current_weather in sorted_locations:
        result += f"{location} - {current_weather[0]}\n"
    return result


print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))


#Rainy
