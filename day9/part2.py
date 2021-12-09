#!/usr/bin/env python3

from math import prod

def compute_basin(i, j, grid):
    """
    Basin starts from the low point and includes any point up, down, left,
    right as long as that point is lower than the point next to it.  9 is
    automatically not included.

    From each point that is in the basin, we have to recursively compute
    the basin to the up, down, left, and right.
    """

    basin = set([(i,j)])

    # up
    for k in range(i - 1, -1, -1):
        if grid[k][j] == 9 or grid[k][j] < grid[i][j]:
            break
        elif grid[k][j] > grid[i][j]:
            basin = basin.union(compute_basin(k, j, grid))

    # down
    for k in range(i + 1, len(grid)):
        if grid[k][j] == 9 or grid[k][j] < grid[i][j]:
            break
        elif grid[k][j] > grid[i][j]:
            basin = basin.union(compute_basin(k, j, grid))

    # left
    for k in range(j - 1, -1, -1):
        if grid[i][k] == 9 or grid[i][k] < grid[i][j]:
            break
        elif grid[i][k] > grid[i][j]:
            basin = basin.union(compute_basin(i, k, grid))

    # right
    for k in range(j + 1, len(grid[0])):
        if grid[i][k] == 9 or grid[i][k] < grid[i][j]:
            break
        elif grid[i][k] > grid[i][j]:
            basin = basin.union(compute_basin(i, k, grid))

    return basin

if __name__ == '__main__':
    data = open('input').read().splitlines()

    grid = []

    for row in data:
        newrow = []
        for column in row:
            newrow += [int(column)]
        grid += [newrow]

    basins = []
    for i,row in enumerate(grid):
        for j,val in enumerate(row):
            up, down, left, right = 10, 10, 10, 10

            # up
            if i > 0:
                up = grid[i - 1][j]

            # down
            if i < len(grid) - 1:
                down = grid[i + 1][j]

            # left
            if j > 0:
                left = grid[i][j - 1]

            # right
            if j < len(grid[i]) - 1:
                right = grid[i][j + 1]

            if val < up and val < down and val < left and val < right:
                basins += [compute_basin(i, j, grid)]

    print(prod([len(x) for x in sorted(basins, key=lambda x: len(x), reverse=True)[0:3]]))
