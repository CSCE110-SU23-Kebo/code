"""
A text file contains the names of Texas trees.
Write a program that performs the following:
1. Read the names of the trees from the file
2. Count the types of trees and write the results in a new file
3. Sort the trees by alphabetical order and write the results in a new file
"""

try:
    with open("texas-trees.txt") as trees_data:
        trees = trees_data.readlines()
        trees = [tree_name.strip() for tree_name in trees]
        print(f"List the trees: {trees}")
        trees_count = {}
        for tree in trees:
            trees_count[tree] = trees.count(tree)
        print(f"Dictionary of trees count is: {trees_count}")

        trees_count_sorted = {}
        print(sorted(trees_count))
        for tree in sorted(trees_count):
            trees_count_sorted[tree] = trees_count[tree]
        print(f"The sorted dictionat of trees count is {trees_count_sorted}")

        with open("texas-trees-count.txt", "w") as trees_stats:
            for name, count in trees_count_sorted.items():
                line = f"The count of {name} is {count}\n"
                trees_stats.write(line)
except:
    pass
