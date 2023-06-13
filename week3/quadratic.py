from math import pow
from math import sqrt
from cmath import sqrt as complex_sqrt

"""
Consider a second degree polynomial or Quadratic equation in the form:
ax2 + bx + c = 0
Write a program to compute the number of real roots of a quadratic equation.
"""

"""
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
"""

a, b, c = input("Enter a b c: ").split()
a = float(a)
b = float(b)
c = float(c)

# discriminant = b**2 - 4 * a * c
discriminant = pow(b, 2) - 4 * a * c
print(f"The discriminant is {discriminant}")

"""
# If the discriminant is strictly positive then the equation has two real roots
if discriminant > 0:
    x1 = (-b - sqrt(discriminant)) / 2*a
    x2 = (-b + sqrt(discriminant)) / 2*a
    print(f"The two real roots are: {x1} and {x2}")
else:
    # If the discriminant is zero then the equation has one real root
    if discriminant == 0:
        x = -b / (2*a)
        print(f"The one real root is: {x}")
    else:
    # If the discriminant is negative then the equation has two complex roots
        x1 = (-b - complex_sqrt(discriminant)) / 2*a
        x2 = (-b + complex_sqrt(discriminant)) / 2*a
        print(f"The two complex roots are: {x1} and {x2}")
"""

# If the discriminant is strictly positive then the equation has two real roots
if discriminant > 0:
    x1 = (-b - sqrt(discriminant)) / 2*a
    x2 = (-b + sqrt(discriminant)) / 2*a
    print(f"The two real roots are: {x1} and {x2}")
elif discriminant == 0:
    # If the discriminant is zero then the equation has one real root
    x = -b / (2*a)
    print(f"The one real root is: {x}")
else:
    # If the discriminant is negative then the equation has two complex roots
    x1 = (-b - complex_sqrt(discriminant)) / 2*a
    x2 = (-b + complex_sqrt(discriminant)) / 2*a
    print(f"The two complex roots are: {x1} and {x2}")


