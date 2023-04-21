"""
This program prints a receipt to a customer
"""
# Gas station receipt
fuel_type = input("What is the fuel type? (regular, plus, premium) ")
payment_type = input("What is your card type? (Visa, Mastercard, American Express) ")
number_of_gallons = int(input("What is the number of gallons?"))
car_wash_options = input("Car wash? ")

regular = 4.30
plus = 5.75
premium = 6.00
tax = 6.25

total_amount = regular * number_of_gallons
total_amount = total_amount + (total_amount * 0.0625)

print()
print("\nWelcome to HEB gas station")
print(f"Fuel type: {fuel_type}")
print(f"Payment type: {payment_type}")
print(f"Number of Gallons: {number_of_gallons}")
print(f"Car wash: {car_wash_options}")
print(f"The total amount for the transaction is ${total_amount}")



