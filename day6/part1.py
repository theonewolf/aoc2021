#!/usr/bin/env python3

DAYS = 80

if __name__ == '__main__':
    data = open('input').read().splitlines()

    lanternfish = [int(i) for i in data[0].split(',')]

    print(f'Initial state: {",".join([str(i) for i in lanternfish])}')
    for day in range(DAYS):
        newfish = []
        for i,fish in enumerate(lanternfish):
            if fish == 0:
                lanternfish[i] = 6
                newfish += [8]
            else:
                lanternfish[i] -= 1
        lanternfish += newfish

    print(f'Total lanternfish: {len(lanternfish)}')
