#!/usr/bin/env python3

from pprint import pprint

# apply cube 1 onto cube 2, return remaining ON cubes
def cube_intersection(cube1, cube2):
    x1, x2 = cube1[1]
    y1, y2 = cube1[2]
    z1, z2 = cube1[3]
    a1, a2 = cube2[1]
    b1, b2 = cube2[2]
    c1, c2 = cube2[3]

    assert x2 >= x1 and y2 >= y1 and z2 >= z1
    assert a2 >= a1 and b2 >= b1 and c2 >= c1

    overlap = max([min([a2, x2]) - max([a1, x1]) + 1, 0]) * \
              max([min([b2, y2]) - max([b1, y1]) + 1, 0]) * \
              max([min([c2, z2]) - max([c1, z1]) + 1, 0])

    print('---- Overlap ----')
    print(overlap)
    new_cubes1 = cube1[4]
    new_cubes2 = cube2[4]

    print (f'Applying {cube1} onto {cube2}')
    print('-------------------------------------------------------')
    # apply cube1 to cube2
    if cube1[0] == 'on':
        if cube2[0] == 'on':
            new_cubes2 -= overlap
        elif cube2[0] == 'off':
            pass
        else:
            raise 'Unknown state'
    elif cube1[0] == 'off':
        if cube2[0] == 'on':
            new_cubes2 -= overlap
            new_cubes1 -= overlap
        elif cube2[0] == 'off':
            new_cubes1 -= overlap
        else:
            raise 'Unknown state'
    else:
        raise 'Unknown state'

    return new_cubes1, new_cubes2

def valid_cube(cube):
    x1, x2 = cube[1]
    y1, y2 = cube[2]
    z1, z2 = cube[3]

    if x1 < -50: return False
    if x2 > 50: return False

    if y1 < -50: return False
    if y2 > 50: return False

    if z1 < -50: return False
    if z2 > 50: return False

    return True

def apply(cube1, cube2):
    x1, x2 = cube1[1]
    y1, y2 = cube1[2]
    z1, z2 = cube1[3]
    a1, a2 = cube2[1]
    b1, b2 = cube2[2]
    c1, c2 = cube2[3]

    assert x2 >= x1 and y2 >= y1 and z2 >= z1
    assert a2 >= a1 and b2 >= b1 and c2 >= c1

    # thanks: https://stackoverflow.com/a/5556796 --> tweaked slightly
    overlap = max([min([a2, x2]) - max([a1, x1]) + 1, 0]) * \
              max([min([b2, y2]) - max([b1, y1]) + 1, 0]) * \
              max([min([c2, z2]) - max([c1, z1]) + 1, 0])

    if overlap > 0:
        nx1 = max(x1, a1)
        nx2 = min(x2, a2)
        ny1 = max(y1, b1)
        ny2 = min(y2, b2)
        nz1 = max(z1, c1)
        nz2 = min(z2, c2)
        volume = (nx2 - nx1 + 1) * (ny2 - ny1 + 1) * (nz2 - nz1 + 1)
        # Thanks to https://www.reddit.com/r/adventofcode/comments/rlxhmg/2021_day_22_solutions/hpmsls8
        # for making me realize my approach could work --> I was one if statement away
        if cube2[0] == 'on':
            return ['off', (nx1, nx2), (ny1, ny2), (nz1, nz2), volume]
        else:
            return ['on', (nx1, nx2), (ny1, ny2), (nz1, nz2), volume]

    return None

if __name__ == '__main__':
    data = open('input').read().splitlines()
    cubes = []

    for line in data:
        signal = line[0:3].strip()
        x, y, z = line.split(',')
        x, y, z = x.split('=')[1], y.split('=')[1], z.split('=')[1]
        x1, x2 = x.split('..')
        y1, y2 = y.split('..')
        z1, z2 = z.split('..')
        x1, x2, y1, y2, z1, z2 = int(x1), int(x2), int(y1), int(y2), int(z1), int(z2)
        cubes_affected = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
        cubes += [[signal, (x1, x2), (y1, y2) , (z1, z2), cubes_affected]]
        print(cubes[-1])
        if not valid_cube(cubes[-1]):
            del cubes[-1]
        else:
            off_cubes = []
            for i, cube in enumerate(cubes[:-1]):
                off_cube = apply(cubes[-1], cube)
                if off_cube is not None:
                    off_cubes += [off_cube]
            if cubes[-1][0] == 'off':
                del cubes[-1]
            for off_cube in off_cubes:
                cubes.insert(0, off_cube)

    pprint(cubes)
    pprint(sum([cube[4] if cube[0] == 'on' else -cube[4] for cube in cubes]))
