text = input()

try:
    times = int(input())
    print( text*times)

except ValueError:  # expected error is Value error , when we expect an integer, but we receive something else
    print("Variable times must be an integer")


