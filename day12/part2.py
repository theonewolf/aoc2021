#!/usr/bin/env python3

def find_paths(connections, visited):
    paths = 0

    if visited[-1] == 'end':
        print(f'Found path: {visited}')
        return 1 # we found one path

    for c in connections[visited[-1]]:
        # once you leave the start cave, you can never return to it
        if c == 'start':
            continue

        # you can visit a _single_ small cave at most twice; all others once
        if c.islower() and c in visited:
            skip = False
            for node in connections:
                if node.islower() and visited.count(node) >= 2:
                    skip = True
                    break
            if skip:
                continue

        paths += find_paths(connections, visited + [c])

    return paths

if __name__ == '__main__':
    data = open('input').read().splitlines()

    connections = {}
    for line in data:
        a, b = line.split('-')
        if a not in connections:
            connections[a] = []
        if b not in connections:
            connections[b] = []
        connections[a] += [b]
        connections[b] += [a]

    num_paths = find_paths(connections, ['start'])

    print(connections)
    print(num_paths)
