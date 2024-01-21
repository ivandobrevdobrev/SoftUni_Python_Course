text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")



#Solution 2
# occurrences = {}
#
# for letter in input():
#     occurrences[letter] = occurrences.get(letter,0) + 1
#
# for symbol, times in sorted(occurrences.items()):
#     print((f"{symbol}: {times} time/s"))



