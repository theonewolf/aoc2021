#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input1').read().splitlines()
    prev = None
    increased = 0

    for line in data:
        current = int(line)
        if prev:
            if current > prev:
                increased += 1
        prev = current

    print(f'{increased}')
