#Topological sort code tried and tesed for example 22.4-1 ; from TB on page 614

from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        
    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A recursive function to perform DFS starting from vertex v
    def dfs_util(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited, stack)
        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do topological sort. It uses recursive dfs_util()
    def topological_sort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []
        # Call the recursive helper function to store topological sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.dfs_util(i, visited, stack)
        return stack

    # Function to count paths from s to d
    def count_paths(self, s, d):
        # Get topological sort of the graph
        topo_sort = self.topological_sort()
        
        # Initialize all path counts as 0
        path_count = [0] * self.V
        path_count[s] = 1  # The path count of the source to itself is 1
        
        # Process vertices in topological order
        for node in topo_sort:
            # Update counts of all adjacent nodes of 'node'
            for adjacent in self.graph[node]:
                path_count[adjacent] += path_count[node]
        
        return path_count[d]

# Create a graph given in the example
g = Graph(8)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 5)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(5, 7)

# Count the number of paths from vertex 1 ('s') to vertex 6 ('t')
s, t = 1, 6
print("Number of paths from vertex {} to vertex {}: {}".format(s, t, g.count_paths(s, t)))
