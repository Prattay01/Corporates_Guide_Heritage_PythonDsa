def find_max_average(arr, k):
    # Calculate the sum of the very first window of size k
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window across the rest of the array
    for i in range(k, len(arr)):
        # Add the next element entering the window (arr[i])
        # Subtract the element leaving the window (arr[i - k])
        window_sum += arr[i] - arr[i - k]
        
        # Track the maximum sum we've seen so far
        max_sum = max(max_sum, window_sum)
        
    # Divide the maximum sum by k to get the maximum average
    return max_sum / k

# --- Test Case ---
arr = [1, 12, -5, -6, 50, 3]
k = 4

result = find_max_average(arr, k)
print(f"The maximum average of a subarray of length {k} is: {result}")  # Output: 12.75