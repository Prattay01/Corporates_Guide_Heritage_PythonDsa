def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid          # Found! Return index
        elif arr[mid] < target:
            low = mid + 1       # Search right half
        else:
            high = mid - 1      # Search left half
    return -1                   # Not found