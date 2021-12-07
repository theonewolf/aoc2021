#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()

    points = [int(i) for i in data[0].split(',')]

    min_location = None
    min_distance = 1000000000
    for i in range(0,sum(points)//len(points)):
        distances = []
        for point in points:
            distances += [abs(i - point)]

        if sum(distances) < min_distance:
            min_distance = sum(distances)
            min_location = i

    print(f'Min distance {min_distance} at location {min_location}')
