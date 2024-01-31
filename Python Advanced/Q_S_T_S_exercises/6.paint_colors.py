from collections import deque
words = deque(input().split(" "))

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"}
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ""

    for color in (first_word + second_word,second_word + first_word): # check if firs + 2nd or 2nd +1st makes a actual color
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1],second_word[:-1]): # mahame last element of each word
            if el:                                    # ako imame element go slagame po sredata an stringa
                words.insert(len(words) // 2,el)

for color in set(secondary_colors.keys()).intersection(result): #chekvame dali ot Results ima v Secondary_colors. keys
    if not secondary_colors[color].issubset(result):
        result.remove(color)
    # checkvame primerno dali key-a na orange ->{red,yellow} e subset na results ( dali go ima v result). Ako ne, mahame orange
print(result)
