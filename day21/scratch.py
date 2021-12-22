#!/usr/bin/env python3

from collections import Counter

if __name__ == '__main__':
    c = Counter()
    rolls = set()
    for i in range(1,4):
        for j in range (1,4):
            for k in range(1,4):
                rolls.add(i+j+k)
                c.update([i+j+k])
                print(f'{i} + {j} + {k} = {i+j+k}')

    print(rolls)
    print(c)
