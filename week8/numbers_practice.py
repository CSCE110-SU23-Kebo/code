"""
Conversions of number
Number systems practice
"""

print(f"\n\nConversion to base 2 (Binary)")
numbers = [23, 357, 12, 86.4, 86]

for number in numbers:
    try:
        binary_number = bin(number)[2:]
        print(f"{number} in binary is {binary_number}")
    except TypeError:
        print(f"Incorrect type conversion")


print(f"\n\nConversion from base 2 (Binary) to decimal")
numbers = ['1010', '1011', '1100', '101100101', '10111', '1010110']
for number in numbers:
    try:
        decimal_number = int(number, 2) # The base of 2 means that the first argument is a binary number
        print(f"{number} in decimal is {decimal_number}")
    except TypeError:
        print(f"Incorrect type conversion")

print(f"\n\nConversion from decimal to hexadecimal")
numbers = [23, 357, 12, 86.4, 86]

for number in numbers:
    try:
        hexadecimal_number = hex(number)[2:]
        print(f"{number} in hexadecimal is {hexadecimal_number}")
    except TypeError:
        print(f"Incorrect type conversion")

print(f"\n\nConversion from base 16 (Hexadecimal) to decimal")
numbers = ['1010', '1011', '1100', '101100101', '10111', '1010110', 'ABCDEF', 'CAFE', 'BEEF101', 'DEADBEEF']

for number in numbers:
    try:
        decimal_number = int(number, 16) # The base of 16 means that the first argument is a hexadecimal number
        print(f"{number} in decimal is {decimal_number}")
    except TypeError:
        print(f"Incorrect type conversion")

"""
In the hexadecimal system the base is 16:
Numbers (0, 15): 0123456789ABCDEF

23 in binary is 10111
1*2^0 + 1*2^1 + 1*2^2 + 0*2^3 + 1*2^4


23 in hexadecimal is 17
7 * 16^0 + 1 * 16^1

357 in hexadecimal is 165
5 * 16^0 + 6 * 16^1 + 1 * 16^2
"""

# Operation on binary numbers

print(f"Bitwise addtion of binary numebrs")
"""
Rules for binary addition
0 + 0 = 0 
0 + 1 = 1 
1 + 0 = 1 
1 + 1 = 10 

Add 1010 + 1100

        1010
+
        1100
        ------
       10110   = 2^4 + 2^2 + 2^1 = 16 + 4 + 2


Add 1111 + 1110
       111
        1111
+
        1110
        ______
       11101  = 2^4 + 2^3 + 2^2 + 2^0
"""

# Unary operator (NOT)
x = 23
print(f"NOT({x}) = {bin(~23)}")

# Binary operators
# AND, OR, XOR, NOT
# 0 is False, 1 is True

x = 13 #  0b1101
y = 12 # 0b1100

"""
AND
x   y   output
0   0   0
0   1   0
1   0   0
1   1   1
"""

"""    
    1101
AND
    1100
    _____
    1100
"""
print(f"AND: {x} & {y} = {x & y}")
print(f"AND: {bin(x)[2:]} & {bin(y)[2:]} = {bin(x&y)[2:]}")


# Bitwise OR

"""
    1101
OR
    1100
    ____
    1101
"""     
print(f"OR: {x} | {y} = {x | y}")
print(f"OR: {bin(x)[2:]} | {bin(y)[2:]} = {bin(x|y)[2:]}")

# Bitwise XOR

"""
    1101
XOR
    1100
    _____
    0001

"""
print(f"XOR: {x} ^ {y} = {x ^ y}")
print(f"XOR: {bin(x)[2:]} | {bin(y)[2:]} = {bin(x^y)[2:]}")

# Shifting binary numbers
# shift left : x << n
# Muliplication by 2^n

x = 12 # 1100
# 1100 << 3 -> 1100000
print(f"{bin(x)[2:]} << 3 is {bin(x<<3)}")
print(f"{bin(x)[2:]} << 3 is {x<<3}")

"""
Shift right
x >> n
Floor division by 2^n
"""

x = 12 # 1100
# 1100 >> 3 -> 0001
print(f"{bin(x)[2:]} >> 3 is {bin(x>>3)}")
print(f"{bin(x)[2:]} >> 3 is {x>>3}")

x = 25 # 11001
# 11001 >> 3 -> 00011
print(f"{bin(x)[2:]} >> 3 is {bin(x>>3)}")
print(f"{bin(x)[2:]} >> 3 is {x>>3}")