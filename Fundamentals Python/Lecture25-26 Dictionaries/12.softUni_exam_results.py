results = {}

command = input()
submissions = {}
while command != "exam finished":
    if "banned" in command:
        username, banned = command.split("-")
        del results[username]
        command = input()
        continue
    username, language, points = command.split("-")
    points = int(points)

    if username not in results.keys():
        results[username] = points
    else:
        if points > results[username]:
            results[username] = points
    if language not in submissions.keys():
        submissions[language] = 1
    else:
        submissions[language] += 1

    command = input()

print("Results:")
for username,points in results.items():
    print(f"{username} | {points}")
print("Submissions:")
for language,count in submissions.items():
    print(f"{language} - {count}")