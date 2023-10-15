words = input().split()
filtered_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(filtered_words))

#print words on a new line if Lenght is even number