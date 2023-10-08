def convert_to_integer (some_numbers:list):
    converted_nums = []
    for num in some_numbers:
        num = int(num)
        converted_nums.append(num)
    min_num = min(converted_nums)
    max_num = max(converted_nums)
    sum_nums = sum(converted_nums)
    return f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_nums}"


numbers = input().split()
print(convert_to_integer(numbers))
