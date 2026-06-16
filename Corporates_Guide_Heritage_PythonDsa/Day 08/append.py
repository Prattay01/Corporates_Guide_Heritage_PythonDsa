colors = ['red', 'green', 'blue']

colors.append('yellow')
print(colors)   # ['red', 'green', 'blue', 'yellow']

# Appending different data types
colors.append(100)      # ['red', 'green', 'blue', 'yellow', 100]
colors.append([1, 2])   # Appends as a single nested list
print(colors)   # ['red', 'green', 'blue', 'yellow', 100, [1, 2]]

# Common use: building a list dynamically with a loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)   # [1, 4, 9, 16, 25]
