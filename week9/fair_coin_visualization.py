from random import *
import matplotlib.pyplot as graph
import os


def flip_coin (coin_type):
    """Returns a random side of a coin (fair or not fair)"""
    if coin_type == "fair":
        sides = ['head', 'tails'] # Model of fair coin (50%, 50%)
    else:
        sides = ['head', 'head', 'tails', 'head'] # (tails: 25%, heads : 75%)
    return choice(sides) # Random event

def simulation_flips(flips):
    """
    This function performs the simulation of multiple coin flips
    and computes the probabilities of head up and tails up
    """
    heads_count = 0
    tails_count = 0

    for flip in range(1, flips+1):
        side = flip_coin('unfair')
        print (f"One flip number {flip} the side {side} turned up")
        if side == 'head':
            heads_count += 1
        elif side == "tails":
            tails_count += 1
    probability_heads_up = (heads_count / flips * 100)
    probability_tails_up = (tails_count / flips * 100)

    return probability_heads_up, probability_tails_up

def plot_simulation (experiments, probabilities_heads_up, probabilities_tails_up):
    """
    The function plots a line chart of probablities of heads up
    versus probabilities of tails up for multiple experiments of coin flips

    @param experiments
    @param probabilities_heads_up
    @param probabilities_tails_up
    """

    graph.plot(experiments, probabilities_heads_up, marker="o", color='y')
    graph.plot(experiments, probabilities_tails_up, marker="x", color='r')
    graph.grid('c')
    graph.xlabel("Number of experiments")
    graph.ylabel("Probabilities")
    graph.legend()
    graph.title("Fair coin simulation")
    graph.xscale("log")

    try:
        path = "coin_simulation"
        if not os.path.isdir(path): # Check if teh directory "coin_simulation" already exists
            os.mkdir(path) # make a new directory
        os.chdir(path)
    except Exception as bug:
        print(f"Directory creation failure. Error code is: {bug}")
    
    graph.savefig("fair_coin_simulation.jpg")
    graph.show()



def main():
    """
    driver function:
    prompts the user for the number of flips and recturn the count of heads and tails

    10 flips
    100 flips
    1,000 flips
    10,000 flips
    100,000 flips
    1,000,000 flips

    """
    experiments = [10, 10**2, 10**3, 10**4, 10**5, 10**6]
    probabilities_heads_up = []
    probabilities_tails_up = []

    for flips in experiments:
        probability_heads_up, probability_tails_up = simulation_flips(flips)
        probabilities_heads_up.append(probability_heads_up)
        probabilities_tails_up.append(probability_tails_up)

    # print the results
    print(f"Probability of heads up: {probabilities_heads_up}")
    print(f"Probability of tails up: {probabilities_tails_up}")

    plot_simulation(experiments, probabilities_heads_up, probabilities_tails_up)

main()