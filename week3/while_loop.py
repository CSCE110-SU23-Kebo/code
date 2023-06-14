import random

"""
Use a while loop to repeat instructions an unknown number of times, until a condition is met. 
e.g.: ask a user for a number between 1 and 10.
We don't know how many times the user may enter a incorrect, so the program keeps asking while the number is not between 1 and 10. 
If the you know exactly how many times to execute instructions, then use a for loop!
"""

# Ask the use for a number between 1 and 10

# Generate a secret number
secret = random.randint(1, 10)

trials = 1
guess = int(input("Guess the secret number: "))

while guess != secret:
    guess = int(input(f"{guess} is incorrect, Try again!\nGuess the secret number: "))
    trials += 1  # trials = trials + 1
print(f"Congratulations! Your guessed the secret number {secret} after {trials} tries!")