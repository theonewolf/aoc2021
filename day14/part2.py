#!/usr/bin/env python3
# Threw in the towel on this one.  I tried estimating a closed form equation
# for the total characters and then start guessing their distribution, or more
# closed form equations.  Finally, I checked Reddit and understood the most
# common approach was counting pairs.  I just didn't make the mental leap.  I
# also thought about dropping the memory and CPU requirements by simplifying
# the rules, or running them like a state machine.  But I estimated I'd either
# need too much RAM, or over 30 minutes compute at 2 GHz.  So I looked for
# clues online.

# Special thanks for inspiration to:
# https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/hojxeq5/


from math import ceil


def count_pairs(pairs, counts):
    newcounts = counts.copy()

    for k,v in counts.items():
        if counts[k] == 0:
            continue

        leftside = k[0] + pairs[k]
        rightside = pairs[k] + k[1]

        # Increase counts due to the application of this rule
        newcounts[leftside] += counts[k]
        newcounts[rightside] += counts[k]

        # Do not double count---these are removed now, as they have become the
        # left and right side strings now
        newcounts[k] -= counts[k]

    return newcounts


def letter_counts(counts):
    totalcounts = {}

    for pair, count in counts.items():
        first, second = pair[0], pair[1]
        # Another insight here, you need to divide the counts by 2.  This is
        # because the middle letters are getting counted twice as we apply the
        # rules.
        totalcounts[first] = totalcounts.get(first, 0) + count
        totalcounts[second] = totalcounts.get(second, 0) + count

    for letter in totalcounts:
        totalcounts[letter] /= 2

    return totalcounts


if __name__ == '__main__':
    data = open('input').read().splitlines()

    template = list(data[0])
    pairs = {}
    counts = {}

    for line in data[2:]:
        pair, insertion = line.split(' -> ')
        pairs[pair] = insertion
        counts[pair] = 0

    for i in range(len(template) - 1):
        counts[''.join(template[i:i+2])] += 1

    print(f'Starting counts: {counts}')
    for i in range(40):
        counts = count_pairs(pairs, counts)

    totalcounts = letter_counts(counts)
    print(f'Total Counts: {totalcounts}')

    maximum = max(totalcounts.values())
    minimum = min(totalcounts.values())
    # I think it is off by one in either direction due to the counting not
    # being perfect for the last couple letters.
    print(f'Max {maximum} - Min {minimum} = {maximum - minimum}')

    # Tried to estimate distribution, this did not work.  However, the
    # predicted total number of characters is a closed form solution and
    # accurate.
    #predicted_total = 2**40 * 4 - (2**40 - 1)
    #predicted_b = (predicted_total * 5) / 16
    #predicted_h = (predicted_total * 2) / 16
    #print(f'predicted: {predicted_total}')
    #print(f'predicted B: {predicted_b}')
    #print(f'predicted H: {predicted_h}')
