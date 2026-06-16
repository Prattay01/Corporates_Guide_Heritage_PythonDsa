def find_bound(arr, target, find_first):
    low, high = 0, len(arr) - 1
    bound_index = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            bound_index = mid  # Record the index we found
            if find_first:
                # To find the first occurrence, keep searching the left half
                high = mid - 1
            else:
                # To find the last occurrence, keep searching the right half
                low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return bound_index

def count_occurrences(arr, target):
    # Find the first and last positions of the target
    first_idx = find_bound(arr, target, find_first=True)
    
    # If the target isn't in the array at all, return 0
    if first_idx == -1:
        return 0
        
    last_idx = find_bound(arr, target, find_first=False)
    
    # Calculate the total count
    return last_idx - first_idx + 1

# --- Test Case ---
arr = [1, 2, 2, 2, 3, 4]
target = 2

result = count_occurrences(arr, target)
print(f"The number {target} appears {result} times.")  # Output: 3