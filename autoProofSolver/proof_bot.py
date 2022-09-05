# create methods to solve 3 number problems, x + y = z. This will solve easy boards instantly.
# use these methods to create new number lists, replace x and y with z
# might need to create a data type to hold the inputs to a new number, like z contains x + y
# this could be used when showing the proof of a solution. z used to find the answer, z.unpacked to show the solution
# there may be a type well suited to this all reay, or I could use a list of numbers + operators to hold the results
# The print and return values should be seperated; after printing if 

from itertools import combinations

cards = [1, 2, 3, 4]

def pair_sum(some_numbers):
    pairs = list(combinations(some_numbers, 2))
    for pair in pairs:
        temp_cards = some_numbers.copy()
        temp_cards.remove(pair[0])
        temp_cards.remove(pair[1])
        print(temp_cards)

pair_sum(cards)