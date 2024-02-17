def gather_credits(number_of_credits, *course_info):
    gathered_credits = 0
    enrolled_courses = []

    for course, credits in course_info:
        if gathered_credits < number_of_credits:
            if course in enrolled_courses:
                continue
            enrolled_courses.append(course)
            gathered_credits += int(credits)
        else:
            break
    if gathered_credits >= number_of_credits:
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
               f"Courses: {', '.join(sorted(enrolled_courses))}"
    return f"You need to enroll in more courses! You have to gather {number_of_credits - gathered_credits} credits more."





#solution 2
# def gather_credits(number_of_credits, *course_info):
#     gathered_credits = 0
#     enrolled_courses = []
#
#     for course, credits in course_info:
#
#         if gathered_credits >= number_of_credits:
#             break
#         if course not in enrolled_courses:
#             enrolled_courses.append(course)
#             gathered_credits += int(credits)
#     if gathered_credits >= number_of_credits:
#         return f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
#                    f"Courses: {', '.join(sorted(enrolled_courses))}"
#     return f"You need to enroll in more courses! You have to gather {number_of_credits - gathered_credits} credits more."






print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))


print(gather_credits(
    80,
    ("Basics", 27),
))
