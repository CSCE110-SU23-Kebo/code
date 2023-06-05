"""
Write a program that prompts a user for information.
And prints a driver licence for a user.
"""

first_name = input("What is the first name? ")
last_name = input("What is the last name? ")
month = input("What is the month of birth? ")
day = input("What is the day of birth? ")
year = input("What is the year of birth? ")
address = input("What is the address?")

print(f"{'Driver License'.upper():^60}")
date_of_birth = month + '/' + day + '/' + year
expiration_date = "11/26/2024"

print(f"{'DOB:':<5} {date_of_birth:<25}{expiration_date:<30}")
print(f"{'First:':<5}{first_name:<55}")
print(f"{'Last:':<5}{last_name:<55}")
print(f"{'Address:':<5}{address:<55}")