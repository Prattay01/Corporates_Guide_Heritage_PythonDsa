def remove_duplicates(arr):
    # Edge case: An empty array has a length of 0
    if not arr:
        return 0
    
    # Initialize the slow pointer at the first element
    slow = 0
    
    # The fast pointer scans through the array starting from the second element
    for fast in range(1, len(arr)):
        # If we find a value that is different from our last unique value...
        if arr[fast] != arr[slow]:
            slow += 1          # Move the unique marker forward
            arr[slow] = arr[fast]  # Copy the unique value over
            
    # The new length is the index of the slow pointer + 1
    return slow + 1

# --- Test Case ---
arr = [1, 1, 2, 3, 3, 4]
print(f"Original array: {arr}")

new_length = remove_duplicates(arr)

# Slicing the array up to new_length to see the modified unique portion
print(f"Modified array: {arr[:new_length]}")
print(f"New length:     {new_length}")