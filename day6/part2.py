#!/usr/bin/env python3

DAYS = 256

if __name__ == '__main__':
    data = open('input').read().splitlines()

    lanternfish = [int(i) for i in data[0].split(',')]
    buckets = [0 for _ in range(9)]

    for fish in lanternfish:
        buckets[fish] += 1
    
    print(f'Day 0 total lanternfish: {sum(buckets)}')
    print(f'\t{buckets}')

    for day in range(DAYS):
        newbuckets = [0 for _ in buckets]
        
        newbuckets[0] = buckets[1]
        newbuckets[1] = buckets[2]
        newbuckets[2] = buckets[3]
        newbuckets[3] = buckets[4]
        newbuckets[4] = buckets[5]
        newbuckets[5] = buckets[6]
        newbuckets[6] = buckets[7] + buckets[0]
        newbuckets[7] = buckets[8]
        newbuckets[8] = buckets[0]

        buckets = newbuckets
        print(f'Day {day + 1} total lanternfish: {sum(buckets)}')
        print(f'\t{buckets}')

    print(f'Total lanternfish: {sum(buckets)}')
