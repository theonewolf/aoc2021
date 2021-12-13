#!/usr/bin/env python3

def create_grid(dots):
    maxX, maxY = max(dots, key=lambda x: x[0])[0] + 1, max(dots, key=lambda x: x[1])[1] + 1
    grid = [['.' for x in range(maxX + 1)] for y in range(maxY + 1)]

    for x,y in dots:
        grid[y][x] = '#'

    return grid

def foldY(grid, y):
    upperhalf = grid[:y]
    lowerhalf = grid[y:]

    for i in range(len(upperhalf)):
        for j in range(len(upperhalf[0])):
            if upperhalf[i][j] == '#':
                continue
            upperhalf[i][j] = lowerhalf[y - i][j]

    return upperhalf

def foldX(grid, x):
    lefthalf = [row[:x] for row in grid]
    righthalf = [row[x:] for row in grid]

    for i in range(len(lefthalf)):
        for j in range(len(lefthalf[0])):
            if lefthalf[i][j] == '#':
                continue
            lefthalf[i][j] = righthalf[i][x - j]

    return lefthalf

def count_stars(grid):
    count = 0
    for row in grid:
        for col in row:
            if col == '#':
                count += 1
    return count

def gridstr(grid):
    return '\n'.join([''.join(row) for row in grid]).replace('.', ' ')

if __name__ == '__main__':
    data = open('deb_input').read().splitlines()

    paper = []
    dots = []
    folds = []

    for line in data:
        if not line:
            continue

        if line.startswith('fold'):
            instruction, num = line.split('=')
            folds += [(instruction[-1], int(num))]
            continue

        x,y = line.split(',')
        dots += [(int(x),int(y))]


    grid = create_grid(dots)

    # apply first fold
    for fold in folds:
        if fold[0] == 'y':
            print(f'--- Applying fold: {fold} ---')
            grid = foldY(grid, fold[1])
            print(count_stars(grid))
        elif fold[0] == 'x':
            print(f'--- Applying fold: {fold} ---')
            grid = foldX(grid, fold[1])
            print(count_stars(grid))
        else:
            raise 'Unknown fold axis!'

    print(gridstr(grid))
