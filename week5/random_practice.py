"""# 1 Default way import
import random

# 2 Rename a module 
import random as canvas

# 3 import all the definitions from a module
from random import *"""

# 4 import specific definitions from a module
from random import sample, choice, shuffle

"""
Example 1: Guessing game
The goal of the Guessing Game is to guess a secret number between 1 and 100.
The program generates a secret number between 1 and 100.
If the users guess is wrong, the program prompts if the guess is too low or too high and keeps asking for a new number.
The program should count and show the number of guesses.
Draw the flowchart and write the code for this program.
"""
"""
secret =randint(1, 100)
guess = int(input("Enter a number between 1 and 100: "))
counter = 1

while guess != secret:
    if guess < secret:
        print (f"{guess} is too low!")
    else:
        print (f"{guess} is too high!")3
    guess = int(input("Enter a number between 1 and 100: "))
    counter += 1
print(f"Congratulations!\n You guessed the secret number {secret} after {counter} tries.")
"""


students = ["Michael", "Christopher", "Jessica", "Matthew", "Ashley", "Jennifer", "Joshua", "Amanda", "Daniel", "David",
            "James", "Robert", "John", "Joseph", "Andrew", "Ryan", "Brandon", "Jason", "Justin", "Sarah", "William",
            "Jonathan", "Stephanie", "Brian", "Nicole", "Nicholas", "Anthony", "Heather", "Eric", "Elizabeth", "Adam",
            "Megan", "Melissa", "Kevin", "Steven", "Thomas", "Timothy", "Christina", "Kyle", "Rachel", "Laura",
            "Lauren", "Amber", "Brittany", "Danielle", "Richard", "Kimberly", "Jeffrey", "Amy", "Crystal", "Michelle",
            "Tiffany", "Jeremy", "Benjamin", "Mark", "Emily", "Aaron", "Charles", "Rebecca", "Jacob", "Stephen",
            "Patrick", "Sean", "Erin", "Zachary", "Jamie", "Kelly", "Samantha", "Nathan", "Sara", "Dustin", "Paul",
            "Angela", "Tyler", "Scott", "Katherine", "Andrea", "Gregory", "Erica", "Mary", "Travis", "Lisa"]

team_size = int(input("Enter the team size: "))
teams_count = int(input("Enter the number of teams: "))

if team_size*teams_count > len(students):
    print(f"Too many teams: there are not enough students!")
    exit()

for team in range(1, teams_count+1):
    print(f"\n\nBuilding teams of {team_size} out of {len(students)}")
    group = sample(students, team_size)
    team_leader = choice(group)
    print(f"Team #{team}: {group}\t The team leader is {team_leader}") 
    shuffle(group)
    print(f"Team: #{team} shuffled version {group}\n")  

    # Remove the group created from the class
    for name in group:
        students.remove(name)