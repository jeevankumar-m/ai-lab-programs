import heapq

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'E': 1},
    'D': {'G': 7},
    'E': {'G': 3},
    'G': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 5,
    'E': 2,
    'G': 0
}

def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node in visited:
            continue

        visited.add(node)

        for neighbour, edge_cost in graph[node].items():
            new_cost = cost + edge_cost
            new_f = new_cost + heuristic[neighbour]

            heapq.heappush(
                queue,
                (new_f, new_cost, neighbour, path + [neighbour])
            )

    return None, float('inf')


path, cost = a_star('A', 'G')

print("Shortest Path:", " -> ".join(path))
print("Total Cost:", cost)