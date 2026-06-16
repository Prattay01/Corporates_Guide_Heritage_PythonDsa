items = [1, 2, 3, 4, 5]

items.reverse()
print(items)    # [5, 4, 3, 2, 1]

# reversed() returns an iterator (does not modify original)
nums = [10, 20, 30]
for x in reversed(nums):
    print(x)   # 30, 20, 10

# Tip: slicing [::-1] also reverses but creates a NEW list
rev_copy = nums[::-1]   # [30, 20, 10]  (original unchanged)
