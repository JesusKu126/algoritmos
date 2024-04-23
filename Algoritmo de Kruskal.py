class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def kruskal(graph):

    edges = sorted((weight, u, v) for u, neighbors in enumerate(graph) for v, weight in enumerate(neighbors) if u < v)
    
    num_vertices = len(graph)
    uf = UnionFind(num_vertices)
    minimum_spanning_tree = []

    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            minimum_spanning_tree.append((u, v, weight))

    return minimum_spanning_tree

graph = [
    [0, 7, 0, 5, 0, 0, 0],
    [7, 0, 8, 9, 7, 0, 0],
    [0, 8, 0, 0, 5, 0, 0],
    [5, 9, 0, 0, 15, 6, 0],
    [0, 7, 5, 15, 0, 8, 9],
    [0, 0, 0, 6, 8, 0, 11],
    [0, 0, 0, 0, 9, 11, 0]
]

minimum_spanning_tree = kruskal(graph)
for edge in minimum_spanning_tree:
    print(edge)
