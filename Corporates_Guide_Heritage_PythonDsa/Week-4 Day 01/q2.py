class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head, data):
    """
    Inserts a new node with the given data at the end of the linked list.
    Returns the head of the list.
    """
    # 1. Create the new node with the given data
    new_node = Node(data)
    
    # 2. Edge Case: If the list is empty, the new node becomes the head
    if head is None:
        return new_node
    
    # 3. Traverse to the last node of the list
    current = head
    while current.next is not None:
        current = current.next
        
    # 4. Link the old last node's 'next' pointer to the new node
    current.next = new_node
    
    # 5. Return the original head
    return head
