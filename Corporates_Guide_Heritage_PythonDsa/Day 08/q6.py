# a) Print each temperature with its index
temperatures = [22, 35, 18, 40, 28, 15, 33, 27]

print("Temperatures with Index:")
for index, temp in enumerate(temperatures):
    print(f"Index {index}: {temp}")

# b) Count temperatures above 30
count = 0
for temp in temperatures:
    if temp > 30:
        count += 1

print("\nTemperatures above 30:", count)

# c) Use zip() to print names and marks
names = ['Alice', 'Bob', 'Charlie']
marks = [85, 92, 78]

print("\nStudent Marks:")
for name, mark in zip(names, marks):
    print(f"{name} - {mark}")

# d) Remove temperatures <= 25 using while loop
temps = temperatures.copy()

print("\nRemoving temperatures <= 25:")
i = 0
while i < len(temps):
    if temps[i] <= 25:
        removed = temps.pop(i)
        print(f"Removed {removed}: {temps}")
    else:
        i += 1

# e) Multiplication table (1 to 5) as grid
print("\nMultiplication Table (1 to 5)")
print("-" * 30)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()
    