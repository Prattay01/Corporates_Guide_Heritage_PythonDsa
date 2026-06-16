nums = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print(nums[2:5])     # [20, 30, 40]   (index 2,3,4)
print(nums[:4])      # [0, 10, 20, 30]  (from start to index 3)
print(nums[6:])      # [60, 70, 80, 90] (from index 6 to end)
print(nums[::2])     # [0, 20, 40, 60, 80] (every 2nd item)
print(nums[::-1])    # [90, 80, 70, ...0]  (reversed list)
print(nums[1:8:3])   # [10, 40, 70]  (start=1, stop=8, step=3)

# Slicing does NOT modify the original list
sub = nums[2:5]
print(sub)           # [20, 30, 40]
