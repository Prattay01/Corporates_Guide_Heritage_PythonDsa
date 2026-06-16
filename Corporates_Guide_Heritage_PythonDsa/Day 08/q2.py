# Original list
scores = [55, 72, 88, 43, 91, 67, 55, 76]

# f) Count how many times 55 appears originally
print("Count of 55:", scores.count(55))

# a) Append 80
scores.append(80)
print("After append:", scores)

# b) Insert 100 at index 3
scores.insert(3, 100)
print("After insert:", scores)

# c) Remove first occurrence of 55
scores.remove(55)
print("After remove:", scores)

# d) Sort in ascending order
scores.sort()
print("Ascending order:", scores)

# e) Sort in descending order
scores.sort(reverse=True)
print("Descending order:", scores)

# g) Find position of 88
print("Index of 88:", scores.index(88))

# h) Pop the last element
popped_value = scores.pop()
print("Popped value:", popped_value)
print("Remaining list:", scores)