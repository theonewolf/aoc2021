#!/usr/bin/env python3

from pprint import pprint
from random import randint

valid_hallway_positions = [0, 1, 3, 5, 7, 9, 10]
valid_row1 = [3, 7, 11, 15]
valid_row2 = [4, 8, 12, 16]
destinations = {'A': set(3, 4), 'B': set(7,8), 'C': set(11,12), 'D': set(15,16)}

def move(amphipod, destination, amphipods):
    # Check if amphipod can move to destination

def random_move():
    # Choose a random amphipod
    # Choose a random destination
   pass

def monte_carlo():
    # For all amphipods
    # Randomly move
    # If winning game board after any move, return cost
    # If no moves after checking all, reset game board

def create_board(row1, row2):
    amphipods = {}
    
    for location, amphipod in zip(valid_row1, row1):
        amphipods[location] = amphipod

    for location, amphipod in zip(valid_row2, row2):
        amphipods[location] = amphipod

    return amphipods

if __name__ == '__main__':
    data = open('input').read().splitlines()

    amphipods = []
    costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

    for line in data:
        amphipod_row = []
        if 'A' in line or 'B' in line or 'C' in line or 'D' in line:
            line = line.split('#')
            for amphipod in line:
                if amphipod.strip():
                    amphipod_row += [amphipod]
            amphipods += [amphipod_row]

    amphipods = create_board(amphipods[0], amphipods[1])

    pprint(amphipods)
