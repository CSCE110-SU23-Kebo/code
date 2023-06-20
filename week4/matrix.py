"""
Create a 2-Dimensional Arrays using Python lists.
A list is a 1-Dimensional objet
"""

"""
e.g 4 x 3 matrix
1 2 3
4 5 6
7 8 9
10 11 12
"""

import random as matrix_numbers

matrix = list()

"""# Method 1:
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
print(f"The matrix number of rows: {rows}\nThe matrix number of columns: {columns}")

# Method 2:
dimensions = input("Enter the rows and the columns: ").split()
dimensions = [int(dimension) for dimension in dimensions]
rows = dimensions[0]
columns =  dimensions[1]
print(f"The matrix number of rows: {rows}\nThe matrix number of columns: {columns}")"""

# Method 3:
rows, columns = input("Enter the rows and the columns: ").split()
rows =  int(rows)
columns = int(columns)
print(f"The matrix number of rows: {rows}\nThe matrix number of columns: {columns}")

# Generate the matrix content using a sequence of number
start = 1
stop = 1
for row in range(rows):
    start = stop
    stop += columns
    line =  [n for n in range(start, stop)]
    matrix.append(line)
print(f"The full matrix: {matrix}")

# Print the 2-D matrix
for row in range(rows):
    print() # new line between each row
    for column  in range(columns):
        print(f"{matrix[row][column]: <6}", end="")

# Generate a 2-D matrix containing random numbers
matrix_2D = []
for row in range(rows):
    line = [matrix_numbers.randint(100, 10000) for n in range(columns)]
    matrix_2D.append(line)

# Print the 2-D matrix
for row in range(rows):
    print() # new line between each row
    for column  in range(columns):
        print(f"{matrix_2D[row][column]: <6}", end="")

# Multiplication of two matrices A and B
# Example of two matrices (2 x 3) and (3 x 2)

matrix_A_rows =  2
matrix_A_columns = 3
matrix_B_rows =  3
matrix_B_columns = 2

matrix_A = list()
matrix_B = list()
matrix_C = list() 

# Initialize matrix C first!
"""
0 0
0 0
"""

"""
for row in range(matrix_A_rows):
    for column in range(matrix_B_columns):
        for coefficient in range(matrix_A_columns):
            # Multiply the coefficients in matrix_C and matrix_B and store the result in matrix_C
            matrix_C[row][column] = ...
"""
