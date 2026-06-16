# ===== Question 5 =====

print("\n===== Question 5 =====")

# a) Create sets A and B

A = {2, 4, 6, 8, 10, 12}
B = {3, 6, 9, 12, 15}

print("Set A:", A)
print("Set B:", B)

# b) Set Operations

print("\nUnion:")
print(A.union(B))

print("\nIntersection:")
print(A.intersection(B))

print("\nDifference (A - B):")
print(A.difference(B))

print("\nDifference (B - A):")
print(B.difference(A))

print("\nSymmetric Difference:")
print(A.symmetric_difference(B))

# c) Subset, Superset, Disjoint Checks

print("\nSubset Check:")
print("Is A a subset of B?", A.issubset(B))

print("\nSuperset Check:")
print("Is B a superset of A?", B.issuperset(A))

print("\nDisjoint Check:")
print("Are A and B disjoint?", A.isdisjoint(B))

# d) Add and Remove Elements

A.add(14)
print("\nA after adding 14:")
print(A)

B.discard(3)
print("\nB after removing 3:")
print(B)

# e) Remove duplicates from list using set

nums = [5, 1, 3, 5, 2, 1, 4, 3, 5, 2, 6]

unique_nums = set(nums)

print("\nOriginal List:")
print(nums)

print("\nUnique Values:")
print(unique_nums)

# f) Create a frozenset

frozen_A = frozenset(A)

print("\nFrozen Set:")
print(frozen_A)

print("\nTrying to modify frozenset:")

try:
    frozen_A.add(100)
except AttributeError as e:
    print("Error:", e)
    
    