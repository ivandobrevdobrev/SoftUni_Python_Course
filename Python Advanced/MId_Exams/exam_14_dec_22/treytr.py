def students_credits(*students_data):
    credits_info = {}
    total_credits = 0
    for string in students_data:
        course, credits, max_points, diyan_points = string.split("-")
        diyan_credits = int(diyan_points) / int(max_points) * int(credits)
        credits_info[course] = diyan_credits
    return credits_info






print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)