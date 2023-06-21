# Create a set
majors = set() # Set constructor
minors = {'MATH', 'ENG', 'BIO'}

print(f"Set of majors: {majors} contains {len(majors)} items")
print(f"Set of minors: {minors} contains {len(minors)} items")

print(f"Is MATH in the list of majors: {'MATH' in majors}")
print(f"Is MATH not in the list of majors: {'MATH' not in majors}")
print(f"Is MATH in the list of minors: {'MATH' in minors}")

# print(f"The second item in {minors} in {minors[1]}")

# .append() and .extend for lists is equivalent to .add() and update() for sets

majors.add('CS')
print(f"Set of majors: {majors} contains {len(majors)} items")

majors.update(['CS', 'LAW', 'APMS', 'GIST', 'ISEN'])
print(f"Set of majors: {majors} contains {len(majors)} items")

majors.update(['MED', 'MATH', 'PHY', 'GEO', 'ISEN'])
print(f"Set of majors: {majors} contains {len(majors)} items")


#.remove() and .discard()

try:
    majors.remove('LAW')
    print(f"Set of majors: {majors} contains {len(majors)} items")
except:
    print(f"We have a problem!")

try:
    majors.remove('LAW')
    print(f"Set of majors: {majors} contains {len(majors)} items")
except:
    print(f"We have a problem!")

majors.discard('MATH')
print(f"Set of majors: {majors} contains {len(majors)} items")

majors.discard('MATH')
print(f"Set of majors: {majors} contains {len(majors)} items")

