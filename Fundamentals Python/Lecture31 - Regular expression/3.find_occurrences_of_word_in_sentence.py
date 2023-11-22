import re

text = input()
word = input()
pattern = fr'\b{word}\b' # we can use f string to here to search the whole word(variable)
     #Ignorecase staright in the pattern
#pattern = fr'(?i)\b{word}\b'

matches = re.findall(pattern,text,re.IGNORECASE) # to ignore the Upper and lower case of the searched word
print(len(matches))

new_match = re.match(pattern,text,re.IGNORECASE)

print(new_match.group())
