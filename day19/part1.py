#!/usr/bin/env python3

from pprint import pprint
from math import sqrt


# scanner 0 is at 0,0,0
    # match 12 overlapping beacons with scanner N
        # using 4 of them with same distances
            # compute scanner N position absolutely

def distance(p1, p2):
    sum = 0
    for i, v in enumerate(p1):
        sum += (v - p2[i]) ** 2
    return sqrt(sum)

def distances(scanner):
    beacon_distances = {}
    for b1 in scanner:
        for b2 in scanner:
            if b1 == b2: continue
            if b1 in beacon_distances:
                if tuple([b2, b1]) in beacon_distances[b1]: continue
                beacon_distances[b1][tuple([b1, b2])] = distance(b1, b2)
            else:
                beacon_distances[b1] = {}
                beacon_distances[b1][tuple([b1, b2])] = distance(b1, b2)

    return beacon_distances

def find_matching(scanner1, scanner2):
    distances_s1 = distances(scanner1)
    distances_s2 = distances(scanner2)

    matches = {}

    for center1 in scanner1:
        for center2 in scanner2:
            for beacons1, d1 in distances_s1[center1].items():
                for beacons2, d2 in distances_s2[center2].items():
                    if d1 == d2:
                        if (center1, center2) in matches:
                            if beacons1 in matches[center1, center2]:
                                matches[center1, center2][beacons1].add(beacons2)
                            else:
                                matches[center1, center2][beacons1] = set()
                                matches[center1, center2][beacons1].add(beacons2)
                        else:
                            matches[center1, center2] = {}
                            matches[center1, center2][beacons1] = set()
                            matches[center1, center2][beacons1].add(beacons2)

    max_matches = 0
    max_match_set = None
    for center1 in scanner1:
        for center2 in scanner2:
            if (center1, center2) in matches and len(matches[center1, center2]) > max_matches:
                max_matches = len(matches[center1, center2])
                max_match_set = matches[center1, center2]

    # center of reference needs to be added to this
    return max_matches + 1, max_match_set

def align_beacons(b1):
    pprint(b1)

if __name__ == '__main__':
    data = open('test_input').read().splitlines()

    scanner = -1
    scanners = {}
    for line in data:
        if not line:
            continue

        if line.startswith('---'):
            scanner += 1
            continue

        if scanner in scanners:
            scanners[scanner] += [tuple([int(x) for x in line.split(',')])]
        else:
            scanners[scanner] = [tuple([int(x) for x in line.split(',')])]

    matching_sets = set()
    for scanner1 in scanners:
        for scanner2 in scanners:
            if scanner1 == scanner2: continue
            if (scanner1, scanner2) in matching_sets: continue
            matching_sets.add(tuple([scanner1, scanner2]))
            matching_sets.add(tuple([scanner2, scanner1]))
            matching, max_match_set = find_matching(scanners[scanner1], scanners[scanner2])
            if matching >= 12:
                print(f'Scanner {scanner1} matches with scanner {scanner2} with {matching} beacons overlapping')
                align_beacons(max_match_set)
