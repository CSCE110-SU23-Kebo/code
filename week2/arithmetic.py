import math

'''
Problem #1
The diagonal of a polygon is a line segment linking two non-adjacent vertices.
Write a program that asks for the number of sides of a polygon. 
Compute  the number of diagonals.
diagonals = sides * (sides - 3) / 2
Print the result in a full sentence.
'''
'''
sides = int(input("What is the number of sides? ")) # This is an explicit type conversion
print(f"The number of sides is: {sides}")
diagonals = int(sides * (sides-3) / 2)
# e.g. for a square: 4*(4-3) / 2
print(f"The number of diagonals in a polygon of {sides} sides is {diagonals}")
'''

"""
Problem # 2
Write a program that calculates the volume of a cylinder
V = π * radius * radius * height
"""


radius = float(input("What is the radius of the base of the cylinder? "))
height = float(input("What is the height of the cylinder? "))
volume = math.pi * radius * radius * height
volume = math.pi * radius**2 * height
volume = math.pi * math.pow(radius, 2) * height
print(f"The volume of a cylinder of radius {radius} and height {height} is {round(volume, 2)}")


"""
Problem # 3
Write a program that tells if a number is odd or even
even: 2k
odd: 2k+1
k is an integer
"""

# An odd number is a number that is expressed as: 2*k + 1 where k is an integer
# An even number is a number that is expressed as: 2*k where k is an integer

"""
number = int(input("Enter an integer: "))
remainder = number % 2 # The % operator is the modulus
print(f"{number} modulus 2 is {remainder}")
"""

"""
Formatting outputs and alignments
"""
print(f"{'Courses':<60} {'Credit hours':^20}")
print(f"{'CSCE110':<60} {'4':^20}")
print(f"{'CSCE 121: Introduction to Program Design and Concepts':<60} {'3':^20}")
print(f"{'CSCE 2622':<60} {'2':^20}")