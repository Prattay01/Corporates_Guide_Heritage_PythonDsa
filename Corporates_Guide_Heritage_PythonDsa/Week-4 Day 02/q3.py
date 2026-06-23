class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(node, data):
    # Base case: If the current spot is empty, place the new node here
    if node is None:
        return TreeNode(data)
    
    # If data is smaller, recursively insert it into the left subtree
    if data < node.val:
        node.left = insert(node.left, data)
    # If data is larger, recursively insert it into the right subtree
    elif data > node.val:
        node.right = insert(node.right, data)
    
    # If data already exists (data == node.val), we do nothing to avoid duplicates
    return node