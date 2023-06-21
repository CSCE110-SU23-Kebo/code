import random
import string

majors = {'CS', 'EE', 'LAW', 'APMS', 'ISEN', 'GIST', 'BIOL', 'PHYS'}
minors = {'MATH', 'STATS', 'LAW', 'USAR', 'PM', 'ME', 'EE'}
"""
print("\nUnion")
all_disciplines = majors.union(minors)
print(f"All the majors and the minors at TAMU are: {all_disciplines}")

all_disciplines = majors | minors
print(f"All the majors and the minors at TAMU are: {all_disciplines}")

print("\nIntersection")
common_disciplines = majors.intersection(minors)
print(f"Disciplines that are both majors and minors at TAMU are: {common_disciplines}")

common_disciplines = majors & minors
print(f"Disciplines that are both majors and minors  at TAMU are: {common_disciplines}")

print("\nDifference")
majors_only = majors.difference(minors)
print(f"Disciplines only offered as majors are: {majors_only}")

majors_only = majors - minors
print(f"Disciplines only offered as majors are: {majors_only}")

majors_only = majors - common_disciplines
print(f"Disciplines only offered as majors are: {majors_only}")

print("\nSymmetric difference")
majors_minors_only = majors.symmetric_difference(minors)
print(f"Disciplines that cannot be both a major and a minor: {majors_minors_only}")

majors_minors_only = majors ^ minors
print(f"Disciplines that cannot be both a major and a minor: {majors_minors_only}")

majors_minors_only = all_disciplines - common_disciplines
print(f"Disciplines that cannot be both a major and a minor: {majors_minors_only}")

print(f"Are these two sets equal? {majors.symmetric_difference(minors) == all_disciplines - common_disciplines} ")
"""

print("\nComplement")
all_majors = set() # All majors in the USA

# Generate 100 random majors names
for maj in range(100):
    major = [random.choice(string.ascii_uppercase) for n in range(3)]
    major_abbreviation = ""
    major_abbreviation = major_abbreviation.join(major)
    all_majors.add(major_abbreviation)

print(f"\nAll the {len(all_majors)} generated majors are {all_majors}")

all_majors.update(majors)
all_majors.update({'AEO', 'EPB', 'ADD', 'MDA'})

non_TAMU_majors = all_majors - majors
print(f"\n\nThe number of TAMU majors is: {len(majors)}")
print(f"The complement of the TAMU majors contains {len(all_majors-majors)} disciplines: {non_TAMU_majors}")

# Set membership
print(f"\nIs MDA a majors in the USA: {'MDA' in all_majors}")

# Set subset and superset
engineering = {'AEO', 'EPB', 'ADD'}

# Subset
print(f"Are all engineering majors part of the USA majors: {engineering.issubset(all_majors)}")

# Superset
print(f"Are all engineering majors part of the USA majors: {all_majors.issuperset(engineering)}")

# Is disjoint
print(f"Are they are common minors and majors? {not majors.isdisjoint(minors)}")
print(f"Are they are common minors and majors? {any(majors.intersection(minors))} {majors.intersection(minors)}")