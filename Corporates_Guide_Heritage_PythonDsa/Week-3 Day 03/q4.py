def merge_sort(arr, depth=0):
    indent = "  " * depth
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    
    # Division Phase Tracking
    print(f"{indent}Dividing: {arr} -> Left: {arr[:mid]}, Right: {arr[mid:]}")
    
    left = merge_sort(arr[:mid], depth + 1)
    right = merge_sort(arr[mid:], depth + 1)
    
    # Merge Phase Tracking
    merged_result = merge(left, right)
    print(f"{indent}Merged Step: {left} + {right} -> {merged_result}")
    
    return merged_result

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Execution
arr = [8, 3, 5, 4, 2, 7, 1, 6]
print("Initial Array:", arr)
print("\n--- Starting Merge Sort Process ---")
sorted_arr = merge_sort(arr)
print("-----------------------------------\n")
print("Final Sorted Array:", sorted_arr)