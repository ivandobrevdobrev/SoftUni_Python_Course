persons = int(input())
capacity = int(input())

courses = persons // capacity
if persons % capacity != 0:
    courses += 1
print(courses)

# version 2
# courses = ceil(persons / capacity)   from match import ceil   10/4 = 2.5 zkryglqme do 3 courses
#