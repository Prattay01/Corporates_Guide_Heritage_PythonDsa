def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Pass {i+1}: {arr}")
        if not swapped:
            break  # Stop early if the array is already sorted

arr = [29, 10, 14, 37, 13]
print("Initial:", arr)
bubble_sort(arr)