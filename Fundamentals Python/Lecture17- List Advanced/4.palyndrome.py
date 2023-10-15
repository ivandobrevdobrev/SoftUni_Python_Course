def palindrome_check(each_word):
    if each_word == each_word[::-1]:
        return each_word

words = input().split()
palindrome_word = input()

palindrome_list = [word for word in words if palindrome_check(word)]
count_palindrome_word = palindrome_list.count(palindrome_word)

print(palindrome_list)
print(f"Found palindrome {count_palindrome_word} times")