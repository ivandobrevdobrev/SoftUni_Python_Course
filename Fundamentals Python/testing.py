# a = "hello"
#
# if a.isupper():
#     print("yes")
# else:
#     print("lower")

#---------------------

# word ="coding"
# sliced_word = word[0:5] #или word[:5] result is "codin" ,5ия индекс не се взима
# sliced_word_2 = word[2:] #result is "ding" , започва от 2рия индекс до края
# sliced_word_3 = word[0::2] #reslut is "cdn", започва от 0 до края със стъпка 2
# #word[start:end:step]
# sliced_word_2 = word[::] #отначало до края
# print(sliced_word)
# print(sliced_word_2)
# print(sliced_word_3)


#---------------- Set()
# my_text ="iivannov"
# my_new_set = {"ajsdh", "asfja", "afa"}  #creating a set
#
# print(my_new_set)
# print(set(my_text))  #covert my_text as a set and print , result : {'o', 'a', 'v', 'n', 'i'} only single unique symbols

#---------------- COUNT()

# text = "112356"
# print(text.count("1"))   връща 2 , защото 1 го има 2 пъти в стринга

#ASCII

# symbol = "M"
# print(ord(symbol))
# number = 75
# print(chr(number))

number = 5
res = number % 3
print(res)