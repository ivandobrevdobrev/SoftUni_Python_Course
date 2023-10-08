def convert_to_integer (some_numbers:list):
    converted_nums = []
    for num in some_numbers:
        num = int(num)
        converted_nums.append(num)
    return converted_nums


numbers =input().split()
sorted_list = sorted(convert_to_integer(numbers))
print(sorted_list)
