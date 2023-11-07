companies = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employees_id = command.split(" -> ")
    if company_name not in companies.keys():
        companies[company_name] = []
    if employees_id not in companies[company_name] :
        companies[company_name].append(employees_id)

for company_name, employees_id in companies.items():
    print(f"{company_name}")
    for id in employees_id:
        print(f"-- {id}")
