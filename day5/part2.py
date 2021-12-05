#!/usr/bin/env python3

GRID_SIZE = 1000

if __name__ == '__main__':
    data = open('input').read().splitlines()
    grid = [[0 for i in range(GRID_SIZE)] for j in range (GRID_SIZE)]

    for row in data:
        pointA, pointB = row.split(' -> ')
        pointA = [int(i) for i in pointA.split(',')]
        pointB = [int(i) for i in pointB.split(',')]

        # only horizontal and vertical for now

        # horizontal lines
        if pointA[0] == pointB[0]:
            if pointA[1] > pointB[1]:
            # swap points to always draw in ascending order
                pointA, pointB = pointB, pointA
            for i in range(pointA[1], pointB[1] + 1):
                grid[i][pointA[0]] += 1
        # vertical lines
        elif pointA[1] == pointB[1]:
            # swap points to always draw in ascending order
            if pointA[0] > pointB[0]:
                pointA, pointB = pointB, pointA
            for i in range(pointA[0], pointB[0] + 1):
                grid[pointA[1]][i] += 1

        # diagonal lines
        else:
            if pointA[0] > pointB[0] or pointA[1] > pointB[1]:
                pointA, pointB = pointB, pointA

            target = pointA
            # 0 = x, 1 = y
            grid[target[1]][target[0]] += 1

            while target[0] != pointB[0] and target[1] != pointB[1]:
                target[0] += 1 if pointA[0] < pointB[0] else -1
                target[1] += 1 if pointA[1] < pointB[1] else -1
                # 0 = x, 1 = y
                grid[target[1]][target[0]] += 1


    count = 0
    for row in grid:
        for col in row:
            if col >= 2:
                count += 1

    print(f'{count}')
