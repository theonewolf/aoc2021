#!/usr/bin/env python3

if __name__ == '__main__':
    data = open('input').read().splitlines()

    position_counts = [[0,0] for i in range(len(data[0]))]

    print(position_counts)
    print(len(data[0]))
    # Count bits in positions
    for line in data:
        for i,c in enumerate(line):
            print(i)
            position_counts[i][int(c)] += 1

    # Construct bit string
    gamma = ''
    epsilon = ''
    for bit_0, bit_1 in position_counts:
        if bit_0 > bit_1:
            gamma += '0'
            epsilon += '1'
        elif bit_1 > bit_0:
            gamma += '1'
            epsilon += '0'
        else:
            print(f'Impossible: equal counts of 1 and 0 bits: {i}[{bit_0, bit_1}]')
            raise 'EqualCountException'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(f'{gamma} * {epsilon} == {gamma * epsilon}')
