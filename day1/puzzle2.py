#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input1').read().splitlines()
    prev = None
    increased = 0

    for line in range(len(data) - 2):
        current = int(data[line]) + int(data[line + 1]) + int(data[line + 2])
        if prev:
            if current > prev:
                increased += 1
        prev = current

    print(f'{increased}')
