"""
file.read() function returns the entire contents of the file as a single string.
"""
"""with open("cities.txt") as places:
    destinations = places.read()
    print(destinations)"""

"""
<file>.readline() returns the next line of the file, returning the text up to and including the next newline character.
This operation reads a file line-by-line
"""
with open("cities.txt") as places:
    line = places.readline().strip()
    while line != "":
        print(line)
        line = places.readline().strip()

"""
<file>.readlines() reads all the lines of a file and saves them into a list.
"""
with open("cities.txt") as places:
    lines = places.readlines()
    print(f"Output 1: {lines}")
    print(f"Output 2: {lines[::-1]}")
    print(f"Output 3: {lines[3:10]}")
    print(f"Output 4: {lines[-1]}")

    # Remove the leading characters from the list items
    lines = [line.strip() for line in lines]

    print(f"Output 5: {lines}")
    print(f"Output 6: {lines[::-1]}")
    print(f"Output 7: {lines[3:10]}")
    print(f"Output 8: {lines[-1]}")