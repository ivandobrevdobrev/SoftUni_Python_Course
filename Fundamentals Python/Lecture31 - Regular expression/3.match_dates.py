import re
some_string = input()
pattern = r'(\b\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})' # \2 means that we call the second group again

matches = re.findall(pattern, some_string)

 # print(matches)  ->  [('13', '/', 'Jul', '1928'), ('10', '-', 'Nov', '1934'), ('25', '.', 'Dec', '1937')] grouped
 #so we need to iterate through the matches to print them in the correct format

for date in matches: # iterate though each Tuple of the list
    day = date[0]
    month = date[2]
    year = date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")

