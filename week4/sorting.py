import random

grades = [random.randint(50, 100) for grages in range(8)]
print(f"Grades: {grades}")
grades.sort(reverse=True)
print(f"Grades: {grades}")
grades.sort(reverse=False)
print(f"Grades: {grades}")

grades = [random.randint(50, 100) for grages in range(8)]
print(f"Grades: {grades}")

ordered_grades = sorted(grades, reverse=True)
print(f"Original grades: {grades}")
print(f"Sorted grades: {ordered_grades}")

ordered_grades = sorted(grades, reverse=False)
print(f"Original grades: {grades}")
print(f"Sorted grades: {ordered_grades}")

print(f"{grades == ordered_grades}")