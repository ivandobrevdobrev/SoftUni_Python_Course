# def a(n):
#     if n <= 0:
#         return
#     print(n)
#     a(n-1)
# a(6)


# factorial

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))
