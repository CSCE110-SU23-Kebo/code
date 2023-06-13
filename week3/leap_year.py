"""
Write a program that asks for a year and classify the year as leap year or not leap year.
Leap years are divisible by 4.
However, years divisible by 100 are not leap years unless they are also divisible by 400.
"""

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")