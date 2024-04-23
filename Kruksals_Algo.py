# Kruksal's algo developed and written for graphs on page no. 632-633 from TB

class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1

def kruskal(graph):
    '''Kruskal's algorithm to find the minimum spanning tree of a graph.'''
    # Sort edges by weight
    edges = sorted(graph['edges'], key=lambda item: item[2])
    
    disjoint_set = DisjointSet(graph['vertices'])
    mst = []

    for edge in edges:
        vertex1, vertex2, weight = edge
        # Check if the selected edge forms a cycle with the mst so far
        if disjoint_set.find(vertex1) != disjoint_set.find(vertex2):
            mst.append(edge)
            disjoint_set.union(vertex1, vertex2)
    
    return mst

# Example graph similar to the provided image
graph = {
    'vertices': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'],
    'edges': set([
        ('0', '1', 4), ('0', '7', 8),
        ('1', '2', 8), ('1', '7', 11),
        ('2', '3', 7), ('2', '5', 4), ('2', '8', 2),
        ('3', '4', 9), ('3', '5', 14),
        ('4', '5', 10),
        ('5', '6', 2),
        ('6', '7', 1), ('6', '8', 6),
        ('7', '8', 7)
    ])
}

mst = kruskal(graph)
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)
