import re

# text = 'the ball _ is big and red and cost 19.30 leva'
# pattern = r'[0-5][0-9]'  # firts num to be between 0-5, second between 0-9
# result = re.findall(pattern,text)
# print(result)



# text = """I am born on 30-Dec-1994.
# My father is born on the 9-Jul-1955.
# 01-July-2000 is not a valid date.
# """
# pattern = r'\b\d{1,2}-[A-Z][a-z]{2}-\d+'  # need only date in format DD-MMM-YYYY
# result = re.findall(pattern,text)
# print(result)
#
# for res in result:
#     print("".join(res))

# findall()
# str = "The rain in Spain"
# x = re.findall("ai", str)
# print(x)

# search()

# str = "The rain in Spain"
# x = re.search("\s", str)
# print("The first white-space character is located in position:", x.start())


#FLAGS
# str = "The rain in Spain"
# print(re.findall("spain",str,re.IGNORECASE))

# text = "somesite"
# new_text = re.sub('some','another',text)
# print(new_text)

email = "ivan9@gmail.com"
pattern = r"[a-z0-9]+"
match = re.findall(pattern,email.split("@")[0])
print(match)
a = email.split("@")[0]
print(a)