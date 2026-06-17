# QUICK SORT - Pivot Selection & Comparison
# Given Array: [15, 3, 9, 8, 5, 2, 7, 1, 6]

def partition(arr, low, high):
    pivot = arr[high]  # Last element as pivot
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


# ---------------- PART A ----------------

arr = [15, 3, 9, 8, 5, 2, 7, 1, 6]

print("PART A: One Pass of Quick Sort")
print("Array Before Partitioning:")
print(arr)

# Perform only one partition pass
temp_arr = arr.copy()
pivot_index = partition(temp_arr, 0, len(temp_arr) - 1)

print("\nArray After Partitioning:")
print(temp_arr)
print("Pivot Element:", temp_arr[pivot_index])
print("Pivot Index:", pivot_index)

# ---------------- FULL QUICK SORT ----------------

sorted_arr = arr.copy()
quick_sort(sorted_arr, 0, len(sorted_arr) - 1)

print("\nFully Sorted Array:")
print(sorted_arr)

# ---------------- PART B ----------------

print("\nPART B: Worst Case of Quick Sort")

worst_case = [1, 2, 3, 4, 5, 6, 7]

print("Worst Case Input:")
print(worst_case)

quick_sort(worst_case, 0, len(worst_case) - 1)

print("After Sorting:")
print(worst_case)

print("\nExplanation:")
print("Quick Sort performs worst when the pivot is always")
print("the smallest or largest element.")
print("Example: Already sorted or reverse sorted arrays.")
print("This creates highly unbalanced partitions and")
print("results in O(n^2) time complexity.")

print("\nHow to Avoid It?")
print("1. Random Pivot Selection")
print("2. Median-of-Three Pivot")
print("3. Hybrid Algorithms like Introsort")