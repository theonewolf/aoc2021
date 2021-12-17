#!/usr/bin/env python3

def step(coordinates, velocity):
    x, y = coordinates
    vx, vy = velocity

    x += vx
    y += vy

    if vx < 0:
        vx += 1
    elif vx > 0:
        vx -= 1

    vy -= 1

    return (x, y), (vx, vy)

def hit(coordinates, target):
    x, y = coordinates
    xb, yb = target
    tx1, tx2 = xb
    ty1, ty2 = yb
    return tx1 <= x and x <= tx2 and ty1 <= y and y <= ty2

def overshot(coordinates, target):
    x, y = coordinates
    xb, yb = target
    tx1, tx2 = xb
    ty1, ty2 = yb
    return y < ty1 or x > tx2

def stalled(coordinates, target, velocity):
    x, y = coordinates
    xb, yb = target
    tx1, tx2 = xb
    ty1, ty2 = yb
    vx, vy = velocity
    return x < tx1 and vx == 0

def compute_max_y(test_vectors, target):
    # Hitting the test target
    candidates = {}
    for start_v in test_vectors:
        coordinates = (0,0)
        v = start_v
        max_y = -1000000000
        #print(f'Coordinates: {coordinates}')
        #print(f'\tVelocity: {v}')
        while not overshot(coordinates, target) and not hit(coordinates, target) and not stalled(coordinates, target, v):
            coordinates, v = step(coordinates, v)
            #print(f'Coordinates: {coordinates}')
            #print(f'\tVelocity: {v}')
            max_y = max(max_y, coordinates[1])
        #if overshot(coordinates, target):
        #    print('Overshot it!')
        if hit(coordinates, target):
        #    print('Hit it!')
            candidates[start_v] = max_y

    max_v, max_y = max(candidates.items(), key=lambda x: x[1])

    return max_y, max_v, len(candidates)

if __name__ == '__main__':
    test = [(20,30), (-10,-5)]
    real = [(60,94), (-171,-136)]

    test_v = [(7,2), (6,3), (9,0), (6,9)]

    # Compute test maximum y
    #max_y, max_v = compute_max_y([(6,9)], test)
    #print(f'Hit target, maximum y = {max_y}, with velocity = {max_v}')

    # Compute real maximum y
    test_v = [(x, y) for x in range(-400, 400, 1) for y in range(-400, 400, 1)]
    max_y, max_v, hitlistlen = compute_max_y(test_v, real)
    print(f'Hit target, maximum y = {max_y}, with velocity = {max_v}')
    print(f'Total initial velocities hitting it: {hitlistlen}')
