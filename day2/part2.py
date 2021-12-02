#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input1').read().splitlines()

    aim = 0
    horizontal = 0
    depth = 0

    for line in data:
        command, quantity = line.split()
        quantity = int(quantity)

        if command == 'up':
            aim -= quantity
        elif command == 'down':
            aim += quantity
        elif command == 'forward':
            horizontal += quantity
            depth += aim * quantity
        else:
            raise 'Error, unknown command!'

    print(f'{horizontal} * {depth} = {horizontal * depth}')
