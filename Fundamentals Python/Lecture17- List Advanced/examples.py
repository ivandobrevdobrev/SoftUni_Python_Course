# nums = [1, 2, 3, 4, 5]
#
# squares = [x ** 2 for x in nums]
# print(squares)
#
# #this is same as
# # for x in nums:
# #     print(x ** 2)
#
# # може да се постави и някакво условие на края If
#
# squares = [x for x in nums if x % 2 == 0]  # gives the Even nums only
# print(squares)
#
# printing_nums = [x for x in range(5)]
# print(printing_nums)
#
# letters = ['a','b','c']
#
# uppercases = [letter.upper() for letter in letters ]
# print(uppercases)
#
# #If else
# nums = [1, 2, 3, 4, 5]
# result =[x ** 2 if x % 2 == 0 else x ** 3 for x in nums]
# print(result)

#sorted
# numbers = [2,5,8,6,9,1,4]
# sort_list = sorted(numbers)
# print(sort_list)
#
# sort_reversed = sorted(numbers,key= lambda x:-x)
# print(sort_reversed)


#  map()

# strings_list = ["1", "2", "3", "4"]
# numbers_list =list(map(int,strings_list))
# print(numbers_list)
#
# names = ['ivan', 'pasho', 'mitko']
# capitalized_names = map(str.capitalize,names)
# print(list(capitalized_names))


#set()

# numbers = [1, 2, 3, 4, 4, 4, 4, 5, 5, 7]
# set_nums = set(numbers)
# print(set_nums)
#
# word = "hello"
# unique_char = set(word)
# print(unique_char)

#merging elements and put as a single element in a list

# text = ["Ivan","is","tall"]
# merged_elements = " ".join(text[0:2])
# text[0:2] = [merged_elements]
# print(text)

#Functions

def calculate(a,b,c=7):
    return  a+b+c

results = calculate(5,8,10)
print(results)
