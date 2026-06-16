def find_all_pairs(arr, target):
    low = 0
    high = len(arr) - 1
    pairs_found = False

    while low < high:
        current_sum = arr[low] + arr[high]

        # Scenario 1: We found a matching pair
        if current_sum == target:
            print(f"({arr[low]}, {arr[high]})")
            pairs_found = True
            # Move both pointers inward to look for other pairs
            low += 1
            high -= 1
            
        # Scenario 2: Sum is too small -> we need a larger value, so move low right
        elif current_sum < target:
            low += 1
            
        # Scenario 3: Sum is too large -> we need a smaller value, so move high left
        else:
            high -= 1

    if not pairs_found:
        print("No pairs found that match the target.")

# --- Test Case ---
arr = [1, 2, 3, 4, 5, 6, 7]
target = 8

print(f"Pairs adding up to {target}:")
find_all_pairs(arr, target)