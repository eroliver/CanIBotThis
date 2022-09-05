# create methods to solve 3 number problems, x + y = z. This will solve easy boards instantly.
# use these methods to create new number lists, replace x and y with z
# might need to create a data type to hold the inputs to a new number, like z contains x + y
# this could be used when showing the proof of a solution. z used to find the answer, z.unpacked to show the solution
# there may be a type well suited to this all reay, or I could use a list of numbers + operators to hold the results
# The print and return values should be seperated; after printing if 

from itertools import combinations, permutations

cards = [1, 2, 3, 4, 5, 6]

def pair_sum(some_numbers):
    pairs = list(combinations(some_numbers, 2))
    for pair in pairs:
        # Copy list of cards, so that no duplicates are used.
        temp_cards = some_numbers.copy()
        # Remove the cards being used as inputs.
        temp_cards.remove(pair[0])
        temp_cards.remove(pair[1])
        if ( pair[0] + pair[1] ) in temp_cards:
            print(f"{pair[0]} + {pair[1]} = {pair[0] + pair[1]}")


def pair_dif(some_numbers):
    pairs = list(permutations(some_numbers, 2))
    for pair in pairs:
        # Copy list of cards, so that no duplicates are used.
        temp_cards = some_numbers.copy()
        # Remove the cards being used as inputs.
        temp_cards.remove(pair[0])
        temp_cards.remove(pair[1])
        if ( pair[0] - pair[1] ) in temp_cards:
            print(f"{pair[0]} - {pair[1]} = {pair[0] - pair[1]}")

def pair_product(some_numbers):
    pairs = list(combinations(some_numbers, 2))
    for pair in pairs:
        # Copy list of cards, so that no duplicates are used.
        temp_cards = some_numbers.copy()
        # Remove the cards being used as inputs.
        temp_cards.remove(pair[0])
        temp_cards.remove(pair[1])
        if ( pair[0] * pair[1] ) in temp_cards:
            print(f"{pair[0]} x {pair[1]} = {pair[0] * pair[1]}")

def pair_quotient(some_numbers):
    pairs = list(permutations(some_numbers, 2))
    for pair in pairs:
        # Copy list of cards, so that no duplicates are used.
        temp_cards = some_numbers.copy()
        # Remove the cards being used as inputs.
        temp_cards.remove(pair[0])
        temp_cards.remove(pair[1])
        if ( pair[0] / pair[1] ) in temp_cards:
            print(f"{pair[0]} / {pair[1]} = { int(pair[0] / pair[1])}")

pair_sum(cards)
pair_dif(cards)
pair_product(cards)
pair_quotient(cards)
