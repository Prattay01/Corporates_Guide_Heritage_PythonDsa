def longest_subarray_sum_less_than_k(arr, k):
    left = 0
    current_sum = 0
    max_length = 0
    
    # Expand the window using the right pointer
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink the window from the left if the sum exceeds K
        while current_sum > k:
            current_sum -= arr[left]
            left += 1
            
        # Update the maximum length found so far
        # The number of elements in the current valid window is (right - left + 1)
        max_length = max(max_length, right - left + 1)
        
    return max_length

# --- Test Case ---
arr = [1, 2, 3, 4, 5]
K = 9

result = longest_subarray_sum_less_than_k(arr, K)
print(f"The length of the longest subarray with sum <= {K} is: {result}")  # Output: 4
