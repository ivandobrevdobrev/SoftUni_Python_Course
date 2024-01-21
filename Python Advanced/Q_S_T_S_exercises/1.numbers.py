# using Set()

set_one = set(input().split())  # if we want to cast into integers --> set(int(el)for el in input().split())
set_two = set(input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()  # *data - опакова, създава лист от данни ->[1,2,3]

    command = first_command + " " + second_command

    if command == "Add First":
        [set_one.add(el) for el in data]
        #set_one.update(data)
    elif command == "Add Second":
        [set_two.add(el) for el in data]
    elif command == "Remove First":
        [set_one.discard(el) for el in data]
    elif command == "Remove Second":
        [set_two.discard(el) for el in data]
    elif command == "Check Subset":
        print((set_one < set_two) or (set_two < set_one))  # set_one.issubset(set_two) or set_two.issubset(set_one)

print(*sorted(map(int, set_one)), sep=", ") # обръщаме към int за да може да се сортират по Judge условие
print(*sorted(map(int, set_two)), sep=", ")


#Solution 2 - using dictionary

# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
# 
# functions = {
#     "Add First": lambda x: [first_set.add(int(el)) for el in x],  # first_set.update(second_set)
#     "Add Second": lambda x: [second_set.add(int(el)) for el in x],
#     "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
#     "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
#     "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
# }
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#
#     command = first_command + " " + second_command
#
#     functions[command](data)
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")