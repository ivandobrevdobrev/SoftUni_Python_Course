schedule = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break
    action = command.split(":")
    lesson = action[1]
    exersice = lesson + "-Exercise"
    if action[0] == "Add":
        if lesson not in schedule:
            schedule.append(lesson)
    elif action[0] == "Insert":
        index = int(action[2])
        if lesson not in schedule:
            schedule.insert(index, lesson)
    elif action[0] == "Remove":
        if lesson in schedule:
            schedule.remove(lesson)
            if exersice in schedule:
                schedule.remove(exersice)
    elif action[0] == "Swap":
        lesson_two = action[2]
        exersice_two = lesson_two + "-Exercise"
        if lesson in schedule and lesson_two in schedule:
            index_one = schedule.index(lesson)
            index_two = schedule.index(lesson_two)
            schedule[index_one], schedule[index_two] = schedule[index_two], schedule[index_one]
            if exersice in schedule:
                schedule.remove(exersice)
                schedule.insert(index_two + 1, exersice)

            if exersice_two in schedule:
                schedule.remove(exersice_two)
                schedule.insert(index_one + 1, exersice_two)

                # idx_exercise_two = schedule.index(exersice_two)
                # schedule[idx_exercise_one],schedule[idx_exercise_two] = schedule[idx_exercise_two],schedule[idx_exercise_one]

    elif action[0] == "Exercise":

        if lesson in schedule and exersice not in schedule:
            index_lesson = schedule.index(lesson)
            schedule.insert(index_lesson + 1,exersice)
        elif lesson not in schedule:
            schedule.append(lesson)
            schedule.append(exersice)

for index, lesson in enumerate(schedule):
    print(f"{index + 1}.{lesson}")
