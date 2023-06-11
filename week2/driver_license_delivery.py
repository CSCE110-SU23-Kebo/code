"""
Part 1
Write a program that asks a user for there age and determines if the user can drive in the State of Texas
"""
"""age = int(input("Enter your age: "))
if age >= 16:
    print("You can get a driver license: ")
else:
    print("Sorry you cannot get a driver license")"""


"""
Add more conditions to issue the driver license
- Age must be at least 16 
- Applicant must have Texas residency (Water bill or electric bill)
- Valid Social security number
"""

# Age check
age = int(input("Enter your age: "))
valid_age = 16 <= age
print(f"Is the age valid: {valid_age}")

# Residency check
water_bill = input("Do you have a water bill? (Yes/No)")
electric_bill = input("Do you have an electric bill? (Yes/No)")
valid_residency = (water_bill.lower() == "yes") or (electric_bill.lower() == "yes")
print(f"Valid residency: {valid_residency}")

# Valid Social Security number
# 9 digits
# Must contains only numbers
SSN = input("Enter your social security number: ")
SSN = SSN.replace(" ", "")
SSN = SSN.replace(".", "")
SSN = SSN.replace("-", "")
valid_SSN = (len(SSN) == 9) and  (SSN.isnumeric())
print(f"Valid SSN: {valid_SSN}")

# Decision on issuing a driver license
if valid_age and valid_residency and valid_SSN:
    print(f"You can get a driver license.")
else:
    print(f"Sorry you cannot get a driver license.")

