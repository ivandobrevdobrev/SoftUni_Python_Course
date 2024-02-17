def team_lineup(*args):
    team_info = {}
    result = ""
    for player, country in args:
        if country not in team_info:
            team_info[country] = []
        team_info[country].append(player)
    sorted_teams = sorted(team_info.items(), key=lambda x: (-len(x[1]), x[0]))
    for country, players in sorted_teams:
        result += f"{country}:\n"
        for player_name in players:
            result += f"  -{player_name}\n"
    return result


print(team_lineup(
    ("Harry Kane", "England"),
    ("Manuel Neuer", "Germany"),
    ("Raheem Sterling", "England"),
    ("Toni Kroos", "Germany"),
    ("Cristiano Ronaldo", "Portugal"),
    ("Thomas Muller", "Germany")))
