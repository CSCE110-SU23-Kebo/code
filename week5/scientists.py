"""
Write a program that asks for multiple scientist names and birth years :)
1. e.g.
Name, birth year: anna, 1998
Name, birth year: taylor, 1996
Name, birth year: eric, 2003
Name, birth year: ashley, 2001
2. Create a dictionary with key name, and value birth year.
3. Next, your program should swap the keys and the values.
4. Sort the dictionary from youngest to oldest student.
"""

# 1 Create the dictionay with items
scientists = {}
entries = int(input("Number of scientists: "))
for scientist in range(entries):
    name = input("Name: ")
    year = int(input("Birth year: "))
    scientists.update({name:year})
print(f"The dictionary of {entries} scientists is : \n{scientists}")

# 2 Swap the keys and the values
reversed_scientists = dict()
for name, year in scientists.items():
    # reversed_scientists[year] = name
    reversed_scientists.update({year:name})
print(f"The reversed dictionary of {entries} scientists is : \n{reversed_scientists}")

# Sort the dictionary from youngest to the eldest
reversed_scientists_sorted = dict()
for year in sorted(reversed_scientists, reverse=True):
    reversed_scientists_sorted[year] = reversed_scientists[year] # Create a new item in the reversed_scientists_sorted dictionary using the sorted years as keys
print(f"The reversed sorted dictionary of {entries} scientists is : \n{reversed_scientists_sorted}")