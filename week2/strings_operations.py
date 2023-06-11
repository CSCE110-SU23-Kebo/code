import string

"""
Create a string
Index a string
Slicing a string
String methods
"""

# Create a string
membership = "yearly subscription, for 2023" # Implicit conversion
year = str(2023) # Explicit conversion
phone = str(9798006818)

# Index a string forward: Acess a part of the string using numbers
print(f"{membership[0]}")
print(f"{membership[1]}")
print(f"{membership[2]}")
print(f"{membership[3]}", end="\n\n")

# Index a string backward: Acess a part of the string using numbers
print(f"{membership[-1]}")
print(f"{membership[-2]}")
print(f"{membership[-3]}")
print(f"{membership[-4]}")

# To break a string down in tokens
tokens1 = membership.split()
print(f"{tokens1}")
tokens2 = membership.split(",")
print(f"{tokens2}")

# Get the size of a string
characters_count = len(phone)
print(f"The nunber of characters in the phone number is {characters_count}")
print(f"The last character in the phone number is {phone[characters_count-1]}, or {phone[-1]} ")

# Slicing a string into substrings
name = "Lionel Messi"
print(f"Name slicing example 1: {name[:]}")
print(f"Name slicing example 2: {name[0:]}")
print(f"Name slicing example 3: {name[2:]}")
print(f"Name slicing example 4: {name[:3]}")
print(f"Name slicing example 5: {name[:-1]}")
print(f"Name slicing example 6: {name[:4]}")

# Add a positive stride or a step to the slice
print(f"Name slicing example 7: {name[::]}")
print(f"Name slicing example 8: {name[::2]}")
print(f"Name slicing example 9: {name[3:7:2]}")

# Add a negative stride or step to the slice
print(f"Name slicing example 10: {name[::-1]}")
print(f"Name slicing example 11: {name[::-3]}")

# The string module
print(string.punctuation)
print(string.ascii_letters)
print(string.digits)

# Phone number area code extraction
'''
phone = input("Enter a 10-digit phone number: ")
phone = phone.replace(" ", "") # Replace all spaces
phone = phone.replace("-", "") # Replace all dashes
phone = phone.replace(".", "") # Replace all dots
print(f"The formatted phone number is : {phone}")
print(f"The area code in {phone} is {phone[:3]}")

print(f"The number of Zeros is: {phone.count('0')}")
print(f"{'9' in phone}")
print(f"Where is 9? {phone.find('9')}")
'''

# Password validation (part 1) using python String methods
password = input("Enter a password: ")
print(f"password.isupper(): {password.isupper()}")
print(f"password.islower(): {password.islower()}")
print(f"password.isalpha(): {password.isalpha()}")
print(f"password.isalphnum(): {password.isalnum()}")
print(f"password.isdigit(): {password.isdigit()}")
print(f"password.isnumeric(): {password.isnumeric()}")

print(f"Uppercase password: {password.upper()}")
print(f"Lowercase password: {password.lower()}")
print(f"Capitalize password: {password.capitalize()}")
print(f"Title password: {password.title()}")


