"""
Examples of functions
"""
import random

# Factorial of a number n
# for n=4, n! = 4 * 3 * 2 * 1 * 0

def factorial(n): # Function definition
    """
    The product of an integer and all the integers below it; e.g. factorial four ( 4! ) is equal to 24.
    """
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
        # fact *= i
    print(f"The factorial of n is {fact}")


# Simulation of gear shift
def gear_shift (number_of_shifts):
    gears = ['first', 'second', 'third', 'fourth', 'fifth', 'reverse']
    gear = random.choice(gears)
    shifts = random.sample(gears, number_of_shifts)
    return shifts

# Function that calculates the distance between two numbers
def calculate_distance (x1, y1, x2, y2):
    """
    This function calculates the distance between two points (x1, y1) (x2,y2)
    """
    x = (x1 - x2) ** 2
    y = (y1 - y2) ** 2
    distance = round(x + y ** (1/2), 2)
    return distance

def entry():
    print("Running From calculator")
    factorial(6)
    gear_shift (4)
    distance = calculate_distance(3.4, 8.9, 46, 9)
    print(f"The distance is: {distance}")
    print(f"The namespace in this program is {__name__}")


if __name__ == "__main__": # If running the program standalone (By itself)
    entry()

    
