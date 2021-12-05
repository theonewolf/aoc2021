#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()
    #data = ['2,2 -> 2,1']
    grid = [[0 for i in range(1000)] for j in range (1000)]

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
        if pointA[1] == pointB[1]:
            # swap points to always draw in ascending order
            if pointA[0] > pointB[0]:
                pointA, pointB = pointB, pointA
            for i in range(pointA[0], pointB[0] + 1):
                grid[pointA[1]][i] += 1
        
        # diagonal lines
        else:
            print('Not a horizontal or vertical line!')

    count = 0
    for row in grid:
        for col in row:
            if col >= 2:
                count += 1

    print(f'{count}')
