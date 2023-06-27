"""
Courses offered in TAMU CSCE for freshman are:
CSCE Course 1: 121
CSCE course 2: 221
Can we swap these two course numbers ?
"""

# This below: will it work?
"""
course_1 = 121
course_2 = 221
print(f"Before the swap of Course 1: {course_1} and Course 2: {course_2}")
course_1 = course_2
course_2 = course_1
print(f"After the swap of Course 1: {course_1} and Course 2: {course_2}")
"""

# Lets try to swap using a temporary variable
print(f"\nMethod 1: using a temporary variable")
course_1 = 121
course_2 = 221
print(f"Before the swap of Course 1: {course_1} and Course 2: {course_2}")
temp = course_1
course_1 = course_2
course_2 = temp
print(f"After the swap of Course 1: {course_1} and Course 2: {course_2}\n")

# Lets try to swap without using a temporary variable
print(f"\nMethod 2: using arithmetic operators (Addition and substraction)")
course_1 = 121
course_2 = 221
print(f"Before the swap of Course 1: {course_1} and Course 2: {course_2}")
course_1 = course_1 + course_2 # 121 + 221 = 343
course_2 = course_1 - course_2 # 343 - 221 = 121
course_1 = course_1 - course_2 # 343 - 121 = 221
print(f"After the swap of Course 1: {course_1} and Course 2: {course_2}\n")

# Lets try to swap without using a temporary variable
print(f"\nMethod 3: using arithmetic operators (Multiplication and Division)")
course_1 = 121
course_2 = 221
print(f"Before the swap of Course 1: {course_1} and Course 2: {course_2}")
course_1 = course_1 * course_2 # 121 * 221 = 26741
course_2 = int(course_1 / course_2) # 26741 / 221 = 121
course_1 = int(course_1 / course_2) # 26741 / 121 = 221
print(f"After the swap of Course 1: {course_1} and Course 2: {course_2}\n")

# Lets try to swap using tuples!
print(f"\nMethod 4: using tuples")
course_1 = 121
course_2 = 221
print(f"Before the swap of Course 1: {course_1} and Course 2: {course_2}")
(course_1, course_2) = (course_2, course_1)
print(f"After the swap of Course 1: {course_1} and Course 2: {course_2}")



