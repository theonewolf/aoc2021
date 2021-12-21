#!/usr/bin/env python3

from math import floor, ceil

def add(left, right):
    return [left] + [right]

# rightfirst only used for adding an exploding value to the left side, rightmost value
def reduce(current, depth=0, operated=False, rightfirst=False, checkleft=False, checkright=False):
    if isinstance(current, int):
        if current > 10 and not operated:
            return [int(floor(current/2)), int(ceil(current/2))], True, False, False
        if not isinstance(operated, bool):
            return current + operated, True, False, False
        return current, operated, False, False

    left, right = current

    if depth >= 4 and not operated and isinstance(left, int) and isinstance(right, int):
        return 0, [left, right], checkleft, checkright

    if not rightfirst:
        left, operated, checkleft, checkright = reduce(left, depth + 1, operated, rightfirst, checkleft, checkright)

        # Handle explosion on left
        if isinstance(operated, list):
            right, _, _, _ = reduce(right, depth + 1, operated[1], rightfirst, checkleft=True)
            return [left, right], operated[0], False, True
        elif not isinstance(operated, bool): # we are the leftmost, nothing to add to the left
            if checkleft:
                operated = True

        right, operated, checkleft, checkright = reduce(right, depth + 1, operated, rightfirst, checkleft, checkright)

        # Handle explosion on right
        if isinstance(operated, list):
            left, _, _, _ = reduce(left, depth + 1, operated[0], rightfirst, checkright=True)
            return [left, right], operated[1], True, False # what about operated[1]???
        elif not isinstance(operated, bool):
            if checkright:
                left, operated, checkleft, checkright = reduce(left, depth + 1, operated, True, checkleft, checkright)
    else:
        right, operated, checkleft, checkright = reduce(right, depth + 1, operated, rightfirst, checkleft, checkright)
        left, operated, checkleft, checkright = reduce(left, depth + 1, operated, rightfirst, checkleft, checkright)

    return [left, right], operated, checkleft, checkright

def test_split(original, target):
    result = split(eval(original))[0]
    passed = True
    if str(result).replace(' ', '') == target:
        print('PASSED: ', end='')
    else:
        print('FAILED: ', end='')
        passed = False

    print(f'split({original}) -> {target}')
    print(f'\tGot: {result}')
    return passed

def test_explosion(original, target):
    result = explosion(eval(original))[0]
    passed = True
    if str(result).replace(' ', '') == target:
        print('PASSED: ', end='')
    else:
        print('FAILED: ', end='')
        passed = False

    print(f'explosion({original}) -> {target}')
    print(f'\tGot: {result}')
    return passed

def magnitude(current):
    if isinstance(current, int):
        return current
    else:
        left, right = current
        return (3 * magnitude(left)) + (2 * magnitude(right))

def test_magnitude(final, target):
    passed = True
    if (magnitude(eval(final))) == target:
        print('PASSED: ', end='')
    else:
        print('FAILED: ', end='')
        passed = False

    print(f'magnitude({final}) == {target}')
    return passed

# walk down the tree, if anything at depth >= 5 replace pair with 0 literal
# walk back up the tree to discover left and right nearest neighbors
def explosion(root, operated=False, depth=0, pair=None, checkleft=False, checkright=False):
    # found a literal
    if isinstance(root, int):
        if checkleft:
            root += pair[0]
        elif checkright:
            root += pair[1]
        return root, operated, depth, pair

    # found a pair
    left, right = root

    # if at depth, we insert a 0 literal for this pair
    # we add the left side to the nearest left neighbor, and right side to the nearest right neighbor
    if not operated and depth >= 4 and isinstance(left, int) and isinstance(right, int):
        return 0, True, depth, [left, right]

    left, operated, depth, pair = explosion(left, operated, depth + 1, pair)
    right, operated, depth, pair = explosion(right, operated, depth + 1, pair)

    return [left] + [right], operated, depth - 1, pair

def split(root, operated=False):
    if isinstance(root, int):
        if not operated and root > 10:
            left, right = int(floor(root / 2)), int(ceil(root / 2))
            operated = True
            return [left, right], operated
        else:
            return root, operated

    left, right = root

    # Find leftmost things first, DFS on left
    left, operated = split(left, operated)
    right, operated = split(right, operated)

    return [left] + [right], operated
            

if __name__ == '__main__':
    data = open('test_input6').read().splitlines()

    numbers = []

    for line in data:
        numbers += [eval(line)]

    #firstrow = numbers[0]
    #print(numbers)
    #for row in numbers[1:]:
    #    print(row)
    #    firstrow = add(firstrow, row)
    #    print(firstrow)
    #    operated = True
    #    while operated:
    #        operated = False
    #        firstrow, operated, _, _ = reduce(firstrow)
    #        if operated: print(firstrow)
    #print(firstrow)

    if not test_magnitude('[9, 1]', 29): exit()
    if not test_magnitude('[1,9]', 21): exit()
    if not test_magnitude('[[9,1],[1,9]]', 129): exit()
    if not test_magnitude('[[1,2],[[3,4],5]]', 143): exit()
    if not test_magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384): exit()
    if not test_magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445): exit()
    if not test_magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791): exit()
    if not test_magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137): exit()
    if not test_magnitude('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488): exit()

    if not test_split('[[[[0,7],4],[15,[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'): exit()
    if not test_split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'): exit()

    if not test_explosion('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'): exit()
    if not test_explosion('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[15,[0,13]]],[1,1]]'): exit()
    if not test_split('[[[[0,7],4],[15,[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,13]]],[1,1]]'): exit()
    if not test_split('[[[[0,7],4],[[7,8],[0,13]]],[1,1]]', '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'): exit()
    if not test_explosion('[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'): exit()
    if not test_explosion('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'): exit()
    if not test_split('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'): exit()

    if not test_explosion('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'): exit()
    if not test_explosion('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'): exit()
    if not test_explosion('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'): exit()
    if not test_explosion('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'): exit()
    if not test_explosion('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'): exit()
