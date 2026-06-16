def binary_search_recursive(arr, target, low, high):
    # Base Case: If the search space is exhausted, the target isn't here
    if low > high:
        return -1
    
    # Calculate the middle index
    mid = (low + high) // 2
    
    # Base Case: Target found
    if arr[mid] == target:
        return mid
    
    # Recursive Case 1: Target is smaller, search the left half
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    
    # Recursive Case 2: Target is larger, search the right half
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# --- Test Case ---
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

# Initial call starts with the full range of the array: index 0 to len(arr) - 1
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Target {target} found at index: {result}")