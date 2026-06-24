from collections import deque

class Graph:
    def __init__(self, is_directed=False):
        """
        Initializes the graph.
        Task 1: Supports switching between Undirected and Directed behavior.
        """
        self.adj_list = {}
        self.is_directed = is_directed

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, u, v):
        """
        Task 1: If self.is_directed is True, only add the forward edge (u -> v).
        """
        self.add_vertex(u)
        self.add_vertex(v)
        
        self.adj_list[u].append(v)
        # Only add the reverse edge if the graph is undirected
        if not self.is_directed:
            self.adj_list[v].append(u)

    def display(self):
        print(f"\n=== Graph Adjacency List ({'Directed' if self.is_directed else 'Undirected'}) ===")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex} -> [{', '.join(neighbors)}]")
        print("==================================================")

    def has_path(self, src, dest):
        """
        Task 2: Checks if a valid path exists between src and dest using BFS.
        """
        if src not in self.adj_list or dest not in self.adj_list:
            return False
            
        visited = set([src])
        queue = deque([src])

        while queue:
            current = queue.popleft()
            if current == dest:
                return True
                
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    def find_connections_within_distance(self, start, distance=2):
        """
        Task 3: Models a social network lookup.
        Finds all unique connections within 'distance' degrees of separation using BFS tracking.
        """
        if start not in self.adj_list:
            return []

        visited = set([start])
        # Queue stores tuples of (person, current_degree_from_start)
        queue = deque([(start, 0)]) 
        connections = []

        while queue:
            current, current_dist = queue.popleft()
            
            # If within target range (excluding the person themselves)
            if 0 < current_dist <= distance:
                connections.append(current)
                
            # If we haven't hit the distance bound, queue neighbors
            if current_dist < distance:
                for neighbor in self.adj_list[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, current_dist + 1))
        return connections

    def count_disconnected_components(self):
        """
        Task 4: Counts total isolated networks/components using an iterative DFS check.
        """
        visited = set()
        component_count = 0

        def _dfs_helper(vertex):
            stack = [vertex]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    # Add unvisited neighbors to stack
                    for neighbor in self.adj_list[curr]:
                        if neighbor not in visited:
                            stack.append(neighbor)

        # Loop through every node in the graph
        for node in self.adj_list:
            if node not in visited:
                # An unvisited node means we stumbled onto a new component
                _dfs_helper(node)
                component_count += 1
                
        return component_count


# ==========================================
# TESTING THE CHALLENGES
# ==========================================
if __name__ == "__main__":
    
    # ---- Task 1 & 3: Social Network Graph (Undirected) ----
    print("--- Running Task 1 & 3 (Social Network Structure) ---")
    social_net = Graph(is_directed=False)
    network_edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    
    for u, v in network_edges:
        social_net.add_edge(u, v)
        
    social_net.display()
    
    # Task 3: Friends and Friends-of-Friends within 2 connections of A
    # Expected: B, C (Direct Friends) and D (Friend-of-Friend)
    hop_2_connections = social_net.find_connections_within_distance('A', distance=2)
    print(f"People within 2 connections of Person A: {hop_2_connections}")


    # ---- Task 2: Path Detection with a Directed Graph Variant ----
    print("\n--- Running Task 2 (Directed Graph Pathfinding) ---")
    directed_graph = Graph(is_directed=True)
    # A -> B -> D -> E -> F, and A -> C -> D
    for u, v in network_edges:
        directed_graph.add_edge(u, v)
        
    directed_graph.display()
    print(f"Path from A to F exists?: {directed_graph.has_path('A', 'F')}") # True
    print(f"Path from F to A exists?: {directed_graph.has_path('F', 'A')}") # False (Edges are one-way)


    # ---- Task 4: Component Breakdown Verification ----
    print("\n--- Running Task 4 (Counting Disconnected Components) ---")
    # Let's use our existing network graph (currently 1 large cluster)
    print(f"Initial connected component count: {social_net.count_disconnected_components()}")
    
    # Now let's add isolated clusters: Person 'X' connected to 'Y' and isolated node 'Z'
    social_net.add_edge('X', 'Y')
    social_net.add_vertex('Z')
    
    social_net.display()
    print(f"Updated component count (Main network + XY island + Z island): {social_net.count_disconnected_components()}")