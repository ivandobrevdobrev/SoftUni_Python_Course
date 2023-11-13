string = input()  # a10m31
letters = ''
new_string = ''
repetitions = ''
unique_symbols = []
for ch in string:
    if not ch.isdigit():
        if not repetitions == "":
            new_string += (letters * int(repetitions))
            letters = ''
            repetitions = ''

        letters += ch.upper()
        unique_symbols.append(ch.lower())
    elif ch.isdigit():
        repetitions += ch
new_string += (letters * int(repetitions)) # слагаме го пак за да може да хване и последите цифри 31 от (a10m31), иначе спира до буквата m
print(f"Unique symbols used: {len(set(unique_symbols))}")
print(new_string)
