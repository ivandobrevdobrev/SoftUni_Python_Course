def is_pallindrome(some_number):
    if some_number == some_number[::-1]:
        return True
    return False
    # може и без да изписваме True nad False и само един ред пишем:
    # return some_number == some_number[::-1]:


numbers = input().split(", ")
for num in numbers:
    print(is_pallindrome(num))
