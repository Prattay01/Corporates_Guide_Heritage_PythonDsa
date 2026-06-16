def max_subarray_sum(arr, k):
    # Step 1: Compute first window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Step 2: Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i]         # Add new element (right)
        window_sum -= arr[i - k]     # Remove old element (left)
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example:
arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_subarray_sum(arr, k))   # Output: 9  (subarray: [5,1,3] -> NO wait [1,5,1] -> NO)
# Windows: [2,1,5]=8  [1,5,1]=7  [5,1,3]=9  [1,3,2]=6  => Max = 9
