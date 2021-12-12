#!/usr/bin/env python3

def find_paths(connections, visited):
    paths = 0

    if visited[-1] == 'end':
        print(f'Found path: {visited}')
        return 1 # we found one path

    for c in connections[visited[-1]]:
        # never visit a lowercased node more than once
        if c.islower() and c in visited:
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
