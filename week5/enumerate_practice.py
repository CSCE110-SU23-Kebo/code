import string
# Enumerate in Python

print(string.ascii_uppercase)
letters = list(string.ascii_uppercase)
print(letters)
letters_enum = enumerate(letters, 6)
print(f"Print the enumeration of letter")
print(f"{list(letters_enum)}")

for letter in enumerate(letters):
    print(f"{letter}\n")

for letter in enumerate(letters, 10):
    print(f"{letter}\n")

letters_tuple = tuple(string.ascii_uppercase)
print(letters_tuple)
for letter in enumerate(letters_tuple):
    print(f"{letter}\n")