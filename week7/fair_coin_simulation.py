from random import *


def flip_coin (coin_type):
    """Returns a random size of a coin (fair or not fair)"""
    if coin_type == "fair":
        sides = ['head', 'tails'] # Model of fair coin (50%, 50%)
    else:
        sides = ['head', 'head', 'tails', 'head'] # (tails: 25%, heads : 75%)
    return choice(sides) # Random event



def main():
    """
    driver function:
    prompts the user for the number of flips and recturn the count of heads and tails
    """
    flips = int(input("Enter the number of coin flips: "))
    heads_count = 0
    tails_count = 0

    for flip in range(1, flips+1):
        side = flip_coin('unfair')
        print (f"One flip number {flip} the side {side} turned up")
        if side == 'head':
            heads_count += 1
        elif side == "tails":
            tails_count += 1

    # print the results
    print(f"Stats \t Heads up count: {heads_count}\t Tails up count: {tails_count}")
    print(f"Probability of heads up: {round(heads_count/flips * 100, 2)}")
    print(f"Probability of tails: {round(tails_count/flips * 100, 2)}")

main()