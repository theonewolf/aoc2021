#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()

    grid = []

    for row in data:
        newrow = []
        for column in row:
            newrow += [int(column)]
        grid += [newrow]

    low_points = []
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
                low_points += [val]


    print(sum([p + 1 for p in low_points]))
