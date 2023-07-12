def remainder(numerator, denominator):
   """
   Implementation of the remainder calculation using the modulus operator
   """
   return numerator % denominator


numerator, denominator = input("Enter numerator and denominator: ").split()
numerator = int(numerator)
denominator = int(denominator)
print(f"The remainder after dividing {remainder(numerator, denominator)}")

print(f"The remainder after dividing {remainder(numerator=100, denominator=30)}")