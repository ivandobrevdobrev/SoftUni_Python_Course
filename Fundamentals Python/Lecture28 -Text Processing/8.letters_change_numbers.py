
alphabet = [chr(x) for x in range(64, 91)]  # create a list of the alphabet A-Z
total_sum = 0
number = ''
letters = []
input_string = [string.strip() for string in input().split()]  #remove redundant spaces in each string

for string in input_string:  # iterate through each string separately
    for symbol in string:    # iterate through each symbol in the string separately
        if symbol.isalpha():  #check first symbol if it is Letter
            letters += symbol
        elif symbol.isdigit(): # if symbol is digit put it in a string "number"
            number += symbol
    if letters[0].isupper(): # check if letter is Upper ot lower cases and do the operation below
        total_sum += int(number) / alphabet.index(letters[0])
    else:
        letters[0]=letters[0].upper()
        total_sum += int(number) * alphabet.index(letters[0])
    if letters[1].isupper():  # do the same check for the 2nd letter and do the operations { we have only 2 letters by default)
        total_sum -= alphabet.index(letters[1])
    else:
        letters[1] = letters[1].upper()
        total_sum += alphabet.index(letters[1])
    number = ''
    letters.clear()

print(f"{total_sum:.2f}")
