from collections import defaultdict


class Graph:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def helper(self, u, visited):
        visited.add(u)
        print(u)
        for v in self.adj[u]:
            if (v not in visited):
                self.helper(v, visited)

    def dfs(self, u):
        visited = set()
        self.helper(u, visited)


g = Graph()

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)

g.dfs(4)
