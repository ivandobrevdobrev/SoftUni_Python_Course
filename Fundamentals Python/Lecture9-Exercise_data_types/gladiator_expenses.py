lost_fights = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_helmet_broken = lost_fights // 2 # на всяка 2ра битка каската се чупи
total_sword_broken = lost_fights // 3 # на всяка 2та битка меча се чупи
total_shield_broken = lost_fights // (2*3) #показва на всяка 2ра и 3та битка. ако искме да разберем на всеки 2ри и 3ти път - това е число което се дели на 2 и 3 , затова ги умножаваме
total_armor_broken = total_shield_broken // 2 # всеки 2ри път когато щита е счупен, бронята се чупи

total_expenses = total_helmet_broken * helmet_price + \
                 total_sword_broken * sword_price + \
                 total_shield_broken * shield_price + \
                 total_armor_broken * armor_price
print(f"Gladiator expenses: {total_expenses:.2f} aureus")
