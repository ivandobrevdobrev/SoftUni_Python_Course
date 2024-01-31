#line = input().split("|")

# sub_list = []
#
# for sub_string in line[::-1]:
#     sub_list.extend(sub_string.split())
# print(*sub_list)

#solution 2

numbers = [string.split() for string in input().split("|")]
print(*[" ".join(sublist) for sublist in numbers[::-1] if sublist])