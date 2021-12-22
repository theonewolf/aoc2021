#!/usr/bin/env python3

from pprint import pprint

# apply cube 1 onto cube 2, return remaining ON cubes
# thanks: https://stackoverflow.com/a/5556796
def cube_intersection(cube1, cube2):
    x1, x2 = cube1[1]
    y1, y2 = cube1[2]
    z1, z2 = cube1[3]
    a1, a2 = cube2[1]
    b1, b2 = cube2[2]
    c1, c2 = cube2[3]

    overlap = max([min([a2, x2]) - max([a1, x1]), 0]) *
              max([min([b2, y2]) - max([b1, y1]), 0]) *
              max([min([c2, z2]) - max([c1, z1]), 0])

    new_cubes1 = cube1[4]
    new_cubes2 = cube2[4]
    if cube2[0] == 'on':
        new_cubes -= overlap # other cube already turned them on...
    elif cube2[0] == 'off':
        new_cubes -= overlap # keep them off...
    else:
        raise 'Unknown state.'

    return new_cubes1, new_cubes2

# TODO
def valid_cube(cube):
    return False

if __name__ == '__main__':
    data = open('test_input').read().splitlines()
    cubes = []

    for line in data:
        signal = line[0:3].strip()
        x, y, z = line.split(',')
        x, y, z = x.split('=')[1], y.split('=')[1], z.split('=')[1]
        x1, x2 = x.split('..')
        y1, y2 = x.split('..')
        z1, z2 = x.split('..')
        x1, x2, y1, y2, z1, z2 = int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)
        cubes_affected = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
        cubes += [[signal, (x1, x2), (y1, y2) , (z1, z2), cubes_affected]]
        if not valid_cube(cubes[-1]):
            del cubes[-1]

    # want to go through all cubes one at a time, and then all cubes already considered
    # for any overlap, BOTH cubes should get their numbers updated
    for i, cube1 in enumerate(cubes):
        for j, cube2 in enumerate(cubes[:i]):
            if i == j: continue
            new_cubes1, new_cubes2 = cube_intersection(cube1, cubes[j])
            cube1[4] = new_cubes1
            cube2[4] = new_cubes2

    pprint(sum([cube[4] for cube in cubes]))
