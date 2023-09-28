n = int(input())
word = input()

full_list =[ ]
new_list =[]

for _ in range(n):
    new_words = input()
    full_list.append(new_words)
    if word in new_words:
        new_list.append(new_words)
print(full_list)
print(new_list)

#solution 2

# for current in full_list:
#     if word == current:
#         new_list.append(current)