#!/usr/bin/env python3

from math import ceil

def compute_distance(positionA, positionB):
    number = abs(positionA - positionB)
    return (number * (number + 1)) / 2

if __name__ == '__main__':
    data = open('input').read().splitlines()

    points = [int(i) for i in data[0].split(',')]

    min_location = None
    min_distance = 2**64-1
    for i in range(0,ceil(sum(points)/len(points)) + 1):
        distances = []
        for point in points:
            distance = compute_distance(point, i)
            #print(f'Point {point} distance {distance} from {i}')
            distances += [distance]

        if sum(distances) < min_distance:
            min_distance = sum(distances)
            min_location = i

    print(f'Min distance {min_distance} at location {min_location}')
