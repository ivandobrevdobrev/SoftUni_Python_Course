# lice na pravoygylnik
# a=int(input())
# b=int(input())
# result =a*b
# print(result)

# Pozdraw po ime

# name = input()
# print ("Hello, ", end = "")
# print(name)
# print("!" )

# price = 5
# items = 3
# discount = 0.21
#
# total = int((price * items * (1-discount)))
#
#
# print(total)
# print(type(total))

# num = 0
# print(abs(num))


#Променлива дефинирана в  programata съществува навсякъде
# command = input()
#
# while command != "stop":
#     print ("ok")
#     name = "ivan"
#     command =input()
#
# print(name)

# for i in range(5):
#     name = "ivan"
#     print(i)
# print(name)

# day = "Monday"
# if day == "Monday":
#     salary = 20
# print(salary)

# for num in range(9, 10):
#     print(num)

# num = 2.4999
# print(f"{num:.0f}")
# print(round(num))

# free_capacity = float(input())
# command = input()
# counter_suitcase = 0
# while not command == "End":
#     size_suitcase = float(command)
#     if free_capacity < size_suitcase:
#         break
#     counter_suitcase = 1
#     if counter_suitcase % 3 == 0:
#         size_suitcase *= 1 + 0.10
#     free_capacity -= size_suitcase
#
#     command = input()
#
# if command == "End":
#     print(f"Congratulations! All suitcases are loaded!")
# else:
#     print("No more space!")
# print(f"Statistic: {counter_suitcase} suitcases loaded.")

# num = 5
# num2 = 2.5
# sum = num+num2
# print(sum)


# current_target_height = 100
# jump_counter=0
# for jumps in range(3):
#     jump_try = int(input())
#     jump_counter += 1
#     if jump_try > current_target_height:
#         highest_jump = jump_try
#         break
# print(jump_counter)

#Clock

#for i in range(0,24):
#   for j in range(0,60):
#       print(f"{i}h:{j}min")

#Пирамида от числа

num = int(input())
current = 1
is_current_bigger_than_num = False


for row in range (num):
   for col in range(1,row+1):
       if current > num:
           is_current_bigger_than_num =True
           break
       print(str(current)+" ", end=" ")
       current += 1
   if is_current_bigger_than_num:
       break
   print()