# 1.Number Definer

# num = float(input())
#
# if num == 0:
#     print("zero")
# elif num > 0:
#     if num < 1:
#         print("small positive")
#     elif num > 1_000_000:
#         print("large positive")
#     else:
#         print("positive")
# elif num < 0:
#     if num > -1:
#         print("small negative")
#     elif abs(num) > 1_000_000:
#         print("large negative")
#     else:
#         print("negative")


    # 2.Max number

# num1, num2, num3 = int(input()),int(input()),int(input())
#
# largest = max(num1, num2, num3)
# print(largest)

# 3.Revrese Word

# word = input()
# for i in range(len(word) - 1, -1, -1):
#     print(word[i], end ="")

# OR using Slice Notation
# print(word[::-1])

                  #4 Even Numbers

# num = int(input())
#
# for i in range(num):
#     new_number = int(input())
#     if new_number % 2 != 0:
#         print(f"{new_number} is odd!")
#         break
# else:
#     print ("All numbers are even.")

                # 5. Number Between 1 and 100

# while True:
#     number = float(input())
#     if 1 <= number <= 100:
#         print(f"The number {number} is between 1 and 100")
#         break


                         #7 Patterns
# number = int(input())
#
# for i in range(1,number+1):
#     for j in range(i):
#         print("*",end="")
#     print()
# for i in range (number-1,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

