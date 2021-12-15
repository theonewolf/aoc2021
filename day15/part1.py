#!/usr/bin/env python3

# Thanks https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Pseudocode 
def dijkstras(graph):
    dist = [[1000000000 for _ in range(len(graph))] for _ in range(len(graph[0]))]
    prev = [[None for _ in range(len(graph))] for _ in range(len(graph[0]))]
    Q = set()

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            Q.add((i,j))

    dist[0][0] = 0

    while not len(Q) == 0:
        min_distance = 10000000000
        u = None
        for i in range(len(dist)):
            for j in range(len(dist[0])):
                if dist[i][j] < min_distance and (i,j) in Q:
                    u = (i,j)
                    min_distance = dist[i][j]
        print(f'u is now {u}, min_distance {min_distance}')
        Q.remove(u)

        i,j = u
        v_up = (i - 1, j)
        v_down = (i  + 1, j)
        v_left = (i, j - 1)
        v_right = (i, j + 1)

        # found target
        if u == (len(graph) - 1, len(graph[0]) - 1):
            break

        for v in [v_up, v_down, v_left, v_right]:
            if v[0] < 0 or v[1] < 0 or v[0] >= len(graph) or v[1] >= len(graph[0]):
                continue
            alt = dist[i][j] + int(graph[v[0]][v[1]])
            print(f'Updating vertex: {v}')
            if alt < dist[v[0]][v[1]]:
                dist[v[0]][v[1]] = alt
                prev[v[0]][v[1]] = u

    return dist, prev

if __name__ == '__main__':
    data = open('input').read().splitlines()
    graph = []

    for line in data:
        graph.append(list(line))

    for row in graph:
        print(row)

    dist, prev = dijkstras(graph)
    print(f'Distance from 0,0 to {len(graph) - 1},{len(graph[0]) - 1} == {dist[len(graph) - 1][len(graph[0]) - 1]}')
