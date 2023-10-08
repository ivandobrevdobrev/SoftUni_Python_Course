def smallest_num(some_numbers: list) -> int: #moje i bez tova int - to e za poqsnenie che shte vrypshtame integers
    return min(some_numbers)


first_num = int(input())
second_num = int(input())
third_num = int(input())
smallest_element = smallest_num([first_num,second_num,third_num])
print(smallest_element)