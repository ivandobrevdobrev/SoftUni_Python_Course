import re

string_map = input()
travel_points = 0
destinations = []
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})(\1)'

matches = re.findall(pattern,string_map)
for match in matches:
    travel_points += len(match[1])
    destinations.append(match[1])          # ['Hawai', 'Cyprus']
# destinations = [location[1] for location in matches] разпакетиране на Тюпъл и слагане в лист -->['Hawai', 'Cyprus']
print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")


