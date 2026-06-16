n = 5

print("--- Pattern A ---")
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()

print("\n--- Pattern B ---")
for row in range(n, 0, -1):
    for col in range(row):
        print("*", end=" ")
    print()

print("\n--- Pattern C ---")
for row in range(1, n + 1):
    for space in range(n - row):
        print(" ", end="")
    for star in range(row):
        print("*", end=" ")
    print()