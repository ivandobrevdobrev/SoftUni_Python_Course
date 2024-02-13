def movie_organizer(*movies_info):
    movies_data ={}
    for movie,genre in movies_info:
        if genre not in movies_data.keys():
            movies_data[genre] = []
        movies_data[genre].append(movie)
    result = ""
    sorted_movies = sorted(movies_data.items(),key=lambda x: (-len(x[1]), x[0]))

    for genre,movies in sorted_movies:
        result += f"{genre} - {len(movies)}\n"
        sorted_keys = sorted(movies)
        for movie in sorted_keys:
            result += f"* {movie}\n"
    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

