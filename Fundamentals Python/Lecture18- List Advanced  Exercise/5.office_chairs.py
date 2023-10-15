def check_rooms(num):
    free_chairs = 0
    for number_of_room in range(1, num +1):
        chairs,visitors = input().split()
        diff = len(chairs) - int(visitors)
        if diff < 0:
            print(f"{abs(diff)} more chairs needed in room {number_of_room}")

        free_chairs += diff

    return free_chairs


count_rooms = int(input())
total_free_chairs = check_rooms(count_rooms)
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")