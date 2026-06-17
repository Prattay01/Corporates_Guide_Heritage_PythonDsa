def insertion_sort_with_count(arr):
    comparisons = 0
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0:
            comparisons += 1  # Count every comparison made in the while condition
            if arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break  # Stops comparing if the correct spot is found
                
        arr[j + 1] = key
        
    return arr, comparisons

# Part A: Already Sorted
array_a = [3, 5, 7, 9, 11]
sorted_a, comps_a = insertion_sort_with_count(array_a.copy())
print("--- Part A: Already Sorted ---")
print(f"Original: {array_a}")
print(f"Sorted:   {sorted_a}")
print(f"Total Comparisons Made: {comps_a}\n")

# Part B: Reverse Sorted
array_b = [11, 9, 7, 5, 3]
sorted_b, comps_b = insertion_sort_with_count(array_b.copy())
print("--- Part B: Reverse Sorted ---")
print(f"Original: {array_b}")
print(f"Sorted:   {sorted_b}")
print(f"Total Comparisons Made: {comps_b}")