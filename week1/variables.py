# A variable is a memory location that stores data

"""
What is a variable?
• A variable is a label for a storage location.
• A variable stores information to be referenced and
manipulated in a computer program.
• A variable holds a value. The value can be a number,
characters, or another type of data.
• A variable can vary by changing what pieces of information it
holds.
"""
# Example #1: This example set the age of a user and computes the age of the user in the next year
# Assignment of 18 to the age variable
age = 18
# Assignment of 2022 to the year variable
year = 2022
# print the age
print(f"Your age in {year} is {age}")

# Compute the age of the user in next year
age = age + 1
year = year + 1
print(f"Your age in {year} is {age}")

# Compute the age of the user in next year
age += 1
year += 1
print(f"Your age in {year} is {age}")

# Compute the age of the user in next year (Not assignment: no update of the variables year and age.)
print(f"Your age in {year+1} is {age+1}")

# Everything in Python is an object.
print(f"Your age is {age}. The type of the variable age is {type(age)}")
print(f"The year is {year}. The type of the variable year is {type(year)}")

# Example 2: Gas price calculation at HEB gas station
gallon_price = 4.30
gallons = 30
print(f"\n\nThe Gallon price is ${gallon_price}\nThe total amount for your purchase is ${gallons*gallon_price}")

# Example 3: create a complex number and print the real part and the imaginary part
number = 3+6j
print(f"The complex number of {number}")
print(f"The real part is {number.real}")
print(f"The imaginary part is {number.imag}")

# Examples 1 , 2 and 3 show the 3 numerical data types in Python
# int, float, complex


