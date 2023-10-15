numbers = list(map(int,input().split(", ")))
#numbers = [int(s) for s in input().split(", ")]

current_group = 10

while numbers: # докато има нещо в листа , когато се изпразни ще брейкне
    filtered_group_current = [number for number in numbers if number <= current_group]
    print(f"Group of {current_group}'s: {filtered_group_current}")
    current_group += 10
    numbers = [number for number in numbers if number not in filtered_group_current]
    #махаме филтрираните чилса от листа и така той се намаля и цикъла ще се върти догато се изпразни