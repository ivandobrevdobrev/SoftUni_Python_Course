
def rounding(some_numbers:list): # функ Параметър, подаваме е някакъв лист
    for i in some_numbers:       #въртим в листа елементите
        num = round(float(i))    #обръщаме всеки елемнт от стринг в float
        new_list.append(num)     # добавяме в новия лист за да принтираме
    return new_list


numbers = input().split()   # четем входни числа и директно в лист (стават на стринг)
new_list = []

print(rounding(numbers))   # викаме Функцията и подаваме аргумент входния ни лист : numbers
