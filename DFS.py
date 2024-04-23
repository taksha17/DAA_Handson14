# dfs implemented for graph (a) on page no. 616 from TB

from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)
        # Time is used to store discovery and finish times
        self.time = 0
        # Discovery and finish times
        self.discovery_time = defaultdict(int)
        self.finish_time = defaultdict(int)

    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A recursive function to perform DFS starting from vertex v
    def dfs_util(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        # Record the discovery time
        self.time += 1
        self.discovery_time[v] = self.time
        print(f"{v} (d: {self.discovery_time[v]})", end=" ")

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

        # Record finish time
        self.time += 1
        self.finish_time[v] = self.time
        print(f"(f: {self.finish_time[v]})", end=" ")

    # The function to do DFS traversal. It uses recursive dfs_util
    def dfs(self, v):
        # Mark all the vertices as not visited
        visited = {i: False for i in self.graph}
        # Call the recursive helper function to print DFS traversal
        self.dfs_util(v, visited)

# Create a graph given in the example
g = Graph()
g.add_edge('a', 'b')
g.add_edge('a', 'e')
g.add_edge('b', 'c')
g.add_edge('b', 'e')
g.add_edge('c', 'd')
g.add_edge('d', 'c')
g.add_edge('e', 'b')
g.add_edge('e', 'd')

# Perform DFS starting from vertex 'a'
print("DFS starting from vertex 'a':")
g.dfs('a')
