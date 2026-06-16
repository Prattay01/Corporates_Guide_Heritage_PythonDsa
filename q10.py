def search_matrix(matrix, target):
    # Edge case: Check if the matrix is empty
    if not matrix or not matrix[0]:
        return False
        
    m = len(matrix)     # Number of rows
    n = len(matrix[0])  # Number of columns
    
    # Start at the top-right corner
    row = 0
    col = n - 1
    
    while row < m and col >= 0:
        current = matrix[row][col]
        
        # Scenario 1: Target found!
        if current == target:
            return True
            
        # Scenario 2: Target is smaller than current element. 
        # Since the column is sorted top-to-bottom, everything below this is also too big.
        # Move LEFT.
        elif target < current:
            col -= 1
            
        # Scenario 3: Target is larger than current element.
        # Since the row is sorted left-to-right, everything to the left is also too small.
        # Move DOWN.
        else:
            row += 1
            
    return False

# --- Test Case ---
matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
target = 5

result = search_matrix(matrix, target)
print(f"Target {target} found in matrix: {result}")  # Output: True