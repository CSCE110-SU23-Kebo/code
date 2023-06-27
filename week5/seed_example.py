import random as numbers_game

# Seed number is 2 and is used to generate a sequence of pseudorandom numbers
# Non determinism
numbers_game.seed(2)

for n in range(10):
    print(numbers_game.random())
    print(numbers_game.random())