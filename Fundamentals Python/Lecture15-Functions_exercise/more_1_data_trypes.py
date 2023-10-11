def read_line(some_word:str):
    if some_word == "int":
        number = int(input())
        return number * 2
    elif some_word == "real":
        number = float(input())
        output = number * 1.5
        return f"{output:.2f}"
    elif some_word == "string":
        string_word = input()
        return "$"+string_word+"$"


data_type = input()
print(read_line(data_type))
