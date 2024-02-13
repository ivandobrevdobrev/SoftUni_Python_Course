def students_credits(*students_data):
    MAX_CREDITS = 240
    credits_info = {}
    total_credits = 0
    for string in students_data:
        course, credits, max_points, diyan_points = string.split("-")
        diyan_credits = int(diyan_points) / int(max_points) * int(credits)
        credits_info[course] = diyan_credits
        total_credits += diyan_credits
    sorted_credits_info = sorted(credits_info.items(), key= lambda x: -x[1])
    result = ""

    if total_credits >= MAX_CREDITS:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {(MAX_CREDITS - total_credits):.1f} credits more for a diploma.\n"
    for course,credit_value in sorted_credits_info:
        result += f"{course} - {credit_value:.1f}\n"
    return result





print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
