numbers = list(map(int, input().split()))
message = list(input())
sum_list = []
new_message = []
for nums in numbers:  # сумиране на цифрите в всяко число
    sum = 0
    digit = str(nums)
    for a in digit:
        sum += int(a)
    sum_list.append(sum)

for current_sum in sum_list:               #въртим в листа със сумираните числа
    for idx in range(len(message)):        #въртим в подадения стринг
        if len(message) < current_sum:
            current_sum %= len(message)    #ако стринга е по-малък от числото, продължаваме отначало да въртим
        if idx == current_sum:              # ако индекса = на числото - взимаме символа от индекса и го премахваме
            new_message.append(message[idx])
            message.pop(current_sum)

print("".join(new_message))
