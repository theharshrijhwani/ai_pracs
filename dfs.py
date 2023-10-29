graph = {
    "A": ["B", "D"],
    "B": ["C", "A"],
    "C": ["B", "D"],
    "D": ["A", "C"],
    "E": ["B", "F"],
    "F": ["E", "G"],
    "G": ["E"]
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("-------DFS-------")

dfs(visited, graph, "E")
