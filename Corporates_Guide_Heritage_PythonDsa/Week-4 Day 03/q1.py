class Graph:
    def __init__(self):
        """Initializes an empty graph using an adjacency list (dictionary)."""
        self.adj_list = {}

    def add_vertex(self, v):
        """Adds a new vertex to the graph if it doesn't already exist."""
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        """Adds an undirected edge between vertex u and vertex v."""
        # Ensure both vertices exist in the graph before connecting them
        self.add_vertex(u)
        self.add_vertex(v)
        
        # Since it's an undirected graph, add edges in both directions
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def display(self):
        """Prints the full adjacency list in a clean, readable format."""
        print("=== Graph Adjacency List ===")
        for vertex, neighbors in self.adj_list.items():
            # Join neighbors with commas, or show 'None' if isolated
            neighbors_str = ", ".join(neighbors) if neighbors else "None"
            print(f"{vertex} -> [{neighbors_str}]")
        print("============================\n")


# --- Testing and Graph Construction ---
if __name__ == "__main__":
    # Initialize the graph
    my_graph = Graph()

    # Define the mandatory edges
    edges_to_add = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'D'),
        ('D', 'E'),
        ('E', 'F')
    ]

    # Add edges to build the network
    for u, v in edges_to_add:
        my_graph.add_edge(u, v)

    # Display the final graph
    my_graph.display()