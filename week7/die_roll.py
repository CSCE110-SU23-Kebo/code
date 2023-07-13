from random import *

def die_roll():
    """
    This function simulates a die roll
    """
    side = randint(1, 6)
    return side

def roll_all_numbers():
    """
    This function simulates multiple die rolls until all sides turn up
    """
    rolls = 0
    dice = [0]*7 # this is a list of length 7 with all zeros
    while sum(dice) != 6:
        side = die_roll()
        dice[side] = 1 # Write a 1 at index side
        rolls += 1
    return rolls

def roll_all_numbers_set():
    """
    This function simulates multiple die rolls until all sides turn up
    """
    rolls = 0
    dice = set()
    while len(dice) != 6:
        side = die_roll()
        dice.add(side)
        rolls += 1
    return rolls




def calculate_average(experiment):
    """
    This function calculates the average number of rolls in multiple experiments
    """
    sum_of_rolls = 0
    for trial in range(experiment):
        sum_of_rolls += roll_all_numbers_set() # Sum up the number of rolls per experiment
    average = sum_of_rolls / experiment
    return average

def main():
    """
    This function calculates on average, the number of times to roll a die before all six numbers turn up.
    """
    experiments = input("Number of experiments: ").split()
    experiments = [int(n) for n in experiments]
    for experiment in experiments:
        average = calculate_average(experiment)
        print(f"Number of experiments: {experiment} -> Average number of rolls is: {average}")

main()