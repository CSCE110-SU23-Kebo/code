import random

"""
For loop practice
"""

game = "mario cart"
for letter in game:
    print(f"character: {letter}")

# Ask for a user's name and print the letters of the name in a table
"""first_name = input("Enter your first name: ")
print(f"{'Letter'.upper():^10}")
for character in first_name:
    print(f"{character.upper():^10}")"""

# Generate 100 random numbers between 0 and 1000
"""for number in range(100):
    random_number = random.randint(0, 1000)
    print(f"Random number is: {random_number}")"""

# Capitalize the first letter in a name:
"""print(f"{'Updated names'.upper():^20}")
for name in ['blake', 'julia', 'marie', 'sylvia', 'anita', 'harshita']:
    print(f"{name.capitalize():^20}")"""

# Generate even numbers between 12 and 110
# Solution 1
"""for number in range(12, 110+1):
    if number % 2 == 0:
        print(f"Even number: {number}")"""

# Solution 2
"""for number in range(12, 110+1, 2):
    print(f"Even number: {number}")"""

# Control statements: break
# Generate even numbers between 12 and 110.
# Additional rules: if we reach 86 the stop.

"""for number in range(12, 110+1, 2):
    print(f"Even number: {number}")
    if number == 86:
        print("End of the loop")
        break"""

# Control statements: continue
# Generate even numbers between 12 and 110.
# Additional rules: if we reach the number 86 print a congratulation message
"""for number in range(12, 110+1, 2):
    if number == 86:
        print(f"Congratulations you win!")
        continue
    print(f"Even number: {number}")"""

# Control statement: pass
# Generate even numbers between 12 and 110.
# Additional rules: if we reach the number 86 Do nothing!
"""for number in range(12, 110+1, 2):
    if number == 86:
        pass # NO OP
    print(f"Even number: {number}")"""


# Else after a loop
"""for age in range(19, 23):
    print (f"Age: {age}")
    if age == 21:
        print(f"Your are {age}! Congratulations buy yourself a beer!")
        break
else:
    print(f"Congratulation you can graduate!")"""


# Nested for loops to print a menu of computer
# Write a program that prints a menu of computer configurations to customers

computers = ["macbook pro", "macbook air", "ipad", "surface"]
operating_systems = ["windows", "linux", "macOS"]
prices = [500.96, 845, 1250, 925]

options = len(computers) * len(operating_systems) * len(prices)
print(f"\nHowdy! Here are all your {options} options")
print(f"{'Computer'.upper():<15}{'Operating System'.upper():<20}{'Price'.upper():<10}")
for computer in computers:
    for os_type in operating_systems:
        for price in prices:
            print(f"{computer:<15}{os_type:<20}{price:<10}")

