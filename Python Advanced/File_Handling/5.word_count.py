import os
import re
words_path = os.path.join("my_folder_resources", "words.txt")
text_path = os.path.join("my_folder_resources", "input.txt")
output_file_path = os.path.join("my_folder_resources", "output.txt")

with open(words_path) as file:
    searched_words_as_text = file.read()  # prochitame vhoda
    searched_words =[word.lower() for word in searched_words_as_text.split()]

with open(text_path) as file :
    content = file.read().lower()  # whole text transfor to lower case

words_count ={}

for searched_word in searched_words:
    pattern = fr"\b{searched_word}\b" # use regex to search for the specific word
    result = re.findall(pattern, content)  # all matched words will go into List -results
    words_count[searched_word] = len(result)

sorted_words_count = sorted(words_count.items(),key=lambda x:-x[1])
print(sorted_words_count)

with open(output_file_path,"a") as file:  # записваме резултата в новия файл, като той автоматично се създава
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")