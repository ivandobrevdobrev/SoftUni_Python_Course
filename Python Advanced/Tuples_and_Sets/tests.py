# my_tuple = ([1,2], [4,5], [10,13])
# my_tuple[0].append(8)
# print(my_tuple)

#Sets


# my_set = {2, 4, 5, 5, 2}  # ще запази само единичните, тези които се повтарят ще ги махне
# print(my_set)
#
# a = set([1, 2, 3, 4])
# b = set([3, 4, 5, 6])
# print(a | b) # Union -> {1, 2, 3, 4, 5, 6}
# print(a.union(b))
# print(a & b) # Intersection -> {3, 4}
# print(a.intersection(b))
# print(a < b) # Subset -> False  дали елемнетите в а срещат ли се в b
# print(a > b) # Superset -> False
# print(a - b) # Difference -> {1, 2} елементите които са в а и не се срещат в b
# print(a.difference(b))
# print(a ^ b) # Symmetric Difference -> {1, 2, 5, 6} елементите които са в а и не се срещат в b, и числата от b които ги няма в а
# print(a.symmetric_difference(b))

numbers = [1, 2, 3, 4, 4, 5, 6, 2, 1]
unique_nums = {num for num in numbers}
print(unique_nums)  #- само уникалните числа 