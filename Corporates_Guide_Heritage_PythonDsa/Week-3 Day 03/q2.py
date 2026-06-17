def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n - 1):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element of unsorted part
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        print(f"Step {i+1}: {arr}")
    return arr

# Execution
arr = [64, 25, 12, 22, 11, 90, 3]
print("Initial Array:", arr)
selection_sort(arr)