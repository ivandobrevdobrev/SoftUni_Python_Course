list_of_fires = input().split("#")
water = int(input())
effort = 0
total_fire =0
cells =["Cells:"]

for current_cell in list_of_fires:
    current_cell = current_cell.split(" = ")

    if current_cell[0] == "High" and 81 <= int(current_cell[1]) <= 125 and (water - int(current_cell[1])) >= 0:
        water -= int(current_cell[1])
        effort += int(current_cell[1]) * 0.25
        total_fire += int(current_cell[1])
        cells.append(current_cell[1])               #качвам ги в Листа като стрингс, да мога да принтирам с .join
    elif current_cell[0] == "Medium" and 51 <= int(current_cell[1]) <= 80 and (water - int(current_cell[1])) >= 0:
        water -= int(current_cell[1])
        effort += int(current_cell[1]) * 0.25
        total_fire += int(current_cell[1])
        cells.append(current_cell[1])               #качвам ги в Листа като стрингс, да мога да принтирам с .join
    elif current_cell[0] == "Low" and 1 <= int(current_cell[1]) <= 50 and (water - int(current_cell[1])) >= 0:
        water -= int(current_cell[1])
        effort += int(current_cell[1]) * 0.25
        total_fire += int(current_cell[1])
        cells.append(current_cell[1])               #качвам ги в Листа като стрингс, да мога да принтирам с .join
print("\n- ".join(cells))                   #принтираме на нов ред с тире отпред
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")