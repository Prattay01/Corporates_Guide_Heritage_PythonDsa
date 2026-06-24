class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def dfs(self, start):
        """
        Performs Depth-First Search starting from the 'start' vertex 
        using recursion.
        """
        visited = set()
        order_of_visit = []

        def _dfs_util(vertex):
            # Mark the node as visited and log its traversal order
            visited.add(vertex)
            order_of_visit.append(vertex)

            # Recursively visit all unvisited neighbors
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    _dfs_util(neighbor)

        if start in self.adj_list:
            _dfs_util(start)
            
        print(f"DFS Traversal Order: {' -> '.join(order_of_visit)}")
        return order_of_visit


# --- Execution ---
if __name__ == "__main__":
    g = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    
    for u, v in edges:
        g.add_edge(u, v)

    # Run DFS starting from vertex A
    g.dfs('A')