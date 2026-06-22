class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Helper method to add elements for our example."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def size(self):
        """
        Traverses the linked list and counts the total number of nodes.
        Returns an integer representing the size.
        """
        count = 0
        current = self.head
        
        # Walk through the list until current becomes None
        while current is not None:
            count += 1
            current = current.next  # Move to the next node
            
        return count