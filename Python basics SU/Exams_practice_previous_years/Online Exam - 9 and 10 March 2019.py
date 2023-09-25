# Задача 5. Световна ранглиста по тенис

# tournaments = int(input())
# initial_points = int(input())
# points_earned = 0
# counter = 0
# for _ in range(tournaments):
#     stage = input()
#     if stage == "W":
#         counter +=1
#         points_earned += 2000
#     elif stage == "F":
#         points_earned += 1200
#     elif stage == "SF":
#         points_earned += 720
#
# print(f"Final points: {initial_points + points_earned}")
# print(f"Average points: {int(points_earned / tournaments)}")
# print((f"{counter/tournaments * 100:.2f}%"))


# Задача 6. Висок скок 70 tochki ot Judge

# target_height = int(input())
# current_target_height = target_height - 30
# highest_jump = 0
# jump_counter = 0
# is_failed = False
# current_try = 0
# while highest_jump <= target_height:
#     for jumps in range(3):
#         jump_try = int(input())
#         current_try = jump_try
#         jump_counter += 1
#         if jump_try > current_target_height:
#             highest_jump = current_try
#             break
#
#     if current_try <= current_target_height:
#         is_failed = True
#         break
#     current_target_height += 5
# if is_failed:
#     print(f"Tihomir failed at {current_target_height}cm after {jump_counter} jumps.")
#
# else:
#     print(f"Tihomir succeeded, he jumped over {target_height}cm after {jump_counter} jumps.")

                          # Задача 6. Баскетболни турнири


# tournaments = input()
# won_matches = 0
# lost_matches = 0
# matches_count = 0
# while tournaments != "End of tournaments":
#     matches = int(input())
#     matches_count += matches
#     for j in range(1, matches + 1):
#         desi_team_points = int(input())
#         other_team_points = int(input())
#         diff = abs(desi_team_points - other_team_points)
#         if desi_team_points > other_team_points:
#             won_matches += 1
#             print(f"Game {j} of tournament {tournaments}: win with {diff} points.")
#         if desi_team_points < other_team_points:
#             lost_matches += 1
#             print(f"Game {j} of tournament {tournaments}: lost with {diff} points.")
#
#     tournaments = input()
# won_matches_percent = won_matches / matches_count * 100
# lost_matches_percent = lost_matches / matches_count * 100
#
# if tournaments == "End of tournaments":
#     print(f"{won_matches_percent:.2f}% matches win")
#     print(f"{lost_matches_percent:.2f}% matches lost")
