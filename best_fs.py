from queue import PriorityQueue

graph = {'A': [('B', 2), ('C', 1)], 'B': [('D', 3), ('E', 4)], 'C': [
    ('F', 5)], 'D': [('G', 1)], 'E': [], 'F': [('H', 3)], 'G': [], 'H': []}

heuristic = {'A': 7, 'B': 6, 'C': 3, 'D': 5, 'E': 4, 'F': 2, 'G': 2, 'H': 0}


def best_fs(graph, start, goal, heuristic):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, [start]))

    while not pq.empty():
        cost, path = pq.get()
        node = path[-1]

        if (node == goal):
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbour, neighbour_cost in graph[node]:
            if neighbour not in visited:
                est_cost = neighbour_cost + heuristic[node]
                new_path = list(path)
                new_path.append(neighbour)
                pq.put((est_cost, new_path))

    return []


start = 'A'
end = 'H'

path = best_fs(graph, start, end, heuristic)

if path:
    print(f"Path from {start} to {end}: {'->'.join(path)}")
else:
    print("nahi hai")
