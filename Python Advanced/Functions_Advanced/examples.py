# def sum_nums(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total
#
# print(sum_nums(2, 5, 8, 10))


# def sum_nums(a,b,*args):
#     total = a+b
#     for num in args:
#         total += num
#     return total
#
# print(sum_nums(2, 5, 8, 10))

# packing dictionaries

# def greet_me(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{value}, {key}")
# greet_me(Peter="Hello", George="Bye")
# greet_me(a=5, b="Bye", c=8)

# unpacking

# def print_nums(a, b, c):
#     print(a, b, c)
#
# some_numbers = [1, 2, 3]
# print_nums(*some_numbers)

# unpacking dictionaries

# def some_func(name, age):
#     print(f"{name} is {age} years old")
#
#
# person = {'age': 20, 'name': "Peter"}
# some_func(**person)


# Advanced Sorting
# a = [3,6,-19, 60 ]
# print(sorted(a, reverse=True))
# print(a)
#
# people = {"George":60, "Mike": 53, "Peter": 43}
# print(sorted(people))
#
# print(sorted(people.items(), key=lambda x:x[1], reverse= True))
# print(sorted(people.items(), key=lambda x:-x[1]))

# def sum():
#     pass
# print(sum.__name__)  izvikvane na imeto na funkciqta

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    finally:
        "execute the code"
