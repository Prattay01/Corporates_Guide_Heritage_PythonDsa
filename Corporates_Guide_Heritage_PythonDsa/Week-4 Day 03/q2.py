from collections import deque

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

    def bfs(self, start):
        """
        Performs Breadth-First Search starting from the 'start' vertex.
        Prints and returns the traversal order.
        """
        if start not in self.adj_list:
            print(f"Vertex {start} not found in graph.")
            return []

        visited = set()
        queue = deque([start])
        visited.add(start)
        order_of_visit = []

        while queue:
            current = queue.popleft()
            order_of_visit.append(current)

            # Explore neighbors in the order they were inserted
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print(f"BFS Traversal Order: {' -> '.join(order_of_visit)}")
        return order_of_visit


# --- Execution ---
if __name__ == "__main__":
    g = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E'), ('E', 'F')]
    
    for u, v in edges:
        g.add_edge(u, v)

    # Run BFS starting from vertex A
    g.bfs('A')