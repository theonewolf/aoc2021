#!/usr/bin/env python3

def step(grid):
    newgrid = grid[:]
    flashed = False
    total_flashes = 0

    # First, the energy level of each octopus increases by 1
    for i,row in enumerate(newgrid):
        for j,col in enumerate(row):
            newgrid[i][j] += 1
            if newgrid[i][j] >= 9:
                flashed = True

    # Then, any octopus with an energy level greater than 9 flashes.
    already_flashed = set()
    # If this causes an octopus to have an energy level greater than 9, it also flashes.
    while flashed:
        flashed = False
        for i,row in enumerate(newgrid):
            for j,col in enumerate(row):
                # An octopus can flash at most once
                if col > 9 and (i,j) not in already_flashed:
                    total_flashes += 1
                    already_flashed.add((i,j))
                    flashed = True

                    # up
                    if i > 0:
                        newgrid[i - 1][j] += 1

                    # down
                    if i < len(newgrid) - 1:
                        newgrid[i + 1][j] += 1

                    # left
                    if j > 0:
                        newgrid[i][j - 1] += 1

                    # right
                    if j < len(newgrid[0]) - 1:
                        newgrid[i][j + 1] += 1

                    # northeast
                    if i > 0 and j < len(newgrid[0]) - 1:
                        newgrid[i - 1][j + 1] += 1

                    # south east
                    if i < len(newgrid) - 1 and j < len(newgrid[0]) - 1:
                        newgrid[i + 1][j + 1] += 1

                    # south west
                    if i < len(newgrid) - 1 and j > 0:
                        newgrid[i + 1][j - 1] += 1

                    # north west
                    if i > 0 and j > 0:
                        newgrid[i - 1][j - 1] += 1

    for i,j in already_flashed:
        newgrid[i][j] = 0

    return total_flashes, newgrid

if __name__ == '__main__':
    data = open('input').read().splitlines()

    grid = []
    for line in data:
        grid.append([int(c) for c in line])

    print(f'--- Initial Grid ---')
    for row in grid:
        print(row)

    total_flashes = 0
    for i in range(100):
        flashes, grid = step(grid)
        total_flashes += flashes

        print(f'--- Step {i+1} ---')
        for row in grid:
            print(row)

    print(f'--- Finished Simulation ---\n')
    print(f'Total flashes: {total_flashes}')
