#!/usr/bin/env python3

from collections import Counter

def step(template, pairs):
    newtemplate = template[:]
    for i in range(len(template)):
        try:
           c1, c2 = template[i], template[i + 1]
           newtemplate.insert(2 * i + 1, pairs[c1 + c2])
        except IndexError:
            return newtemplate
    return newtemplate

if __name__ == '__main__':
    data = open('test_input').read().splitlines()

    template = list(data[0])
    pairs = {}

    for line in data[2:]:
        pair, insertion = line.split(' -> ')
        pairs[pair] = insertion

    for i in range(10):
        print(f'Step: {i}')
        template = step(template, pairs)

    counts = Counter(template)
    print(counts)
    print(len(template))
    print(max(counts.values()) - min(counts.values()))
