import random
import string

"""
Collective data structures:
Lists are sequences used to store collections of data.
Lists are ordered and their elements can be indexed by numbers.
Lists are mutable objects. You can change individual elements in a list.
You can create sub-lists using the slice operators.
Lists are heterogeneous
"""

# creating a list
airports = ['CLL', 'DFW', 'JFK']

# iterate over the content of a list
for airport in airports:
    print(f"The airport is: {airport}")

# Append new airports to airports to the list
new_airports = ['MIA', 'EVV', 'HOU', 'AUS']
for new_airport in new_airports:
    airports.append(new_airport)
print(f"Updated list of airports: {airports} with {len(airports)} items")

# Extend the list of airports
new_airports = ['LAX', 'CHI', 'OMA', 'CDG', 'COO']
airports.extend(new_airports)
print(f"Updated list of airports: {airports} with {len(airports)} items")

# Populate a list dynamically using list comprehension

# Example 1: Create a list of all the even numbers between 0 and 1000
# even_numbers = [expression for iterator in sequence if condition]

# solution1
even_numbers = [2*k for k in range(0, int(1000/2)+1)]
print(f"Even numbers between 0 and 1000 are: {even_numbers}\n")

# solution 2
even_numbers = [k for k in range(0, 1000+1) if k % 2 == 0]
print(f"Even numbers between 0 and 1000 are: {even_numbers}\n\n")


# Example 2: Create a list of all the odd numbers between 0 and 1000
# even_numbers = [expression for iterator in sequence if condition]

# solution1
odd_numbers = [2*k+1 for k in range(0, int(1000/2))]
print(f"Odd numbers between 0 and 1000 are: {odd_numbers}\n")

# solution 2
odd_numbers = [k for k in range(0, 1000) if k % 2 == 1]
print(f"Odd numbers between 0 and 1000 are: {odd_numbers}\n")

# Concatenation of lists:
all_numbers = even_numbers + odd_numbers
print(f"All the numbers between 0 and 1000 are: {all_numbers}")
all_numbers.sort()
print(f"All the numbers between 0 and 1000 (sorted) are: {all_numbers}")

# Multiplication of lists
print()
print(f"The list of even numbers multiplied four times: {even_numbers*4}")

# Secure password Generator
# Generate a password that contains letters and digits using list comprehension
password = [random.choice(string.ascii_letters + string.digits + string.punctuation) for number in range(18)]
password_string = ""
password_string = password_string.join(password)
print(f"\nThe generated password is: {password_string}")

