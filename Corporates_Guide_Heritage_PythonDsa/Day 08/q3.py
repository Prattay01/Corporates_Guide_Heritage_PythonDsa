# a) Squares of numbers from 1 to 15
squares = [x**2 for x in range(1, 16)]
print("Squares:", squares)

# b) All even numbers from 1 to 50
evens = [x for x in range(1, 51) if x % 2 == 0]
print("Even Numbers:", evens)

# c) Words with more than 4 characters
words = ['hello', 'world', 'python', 'is', 'great']
long_words = [word for word in words if len(word) > 4]
print("Words > 4 characters:", long_words)

# d) Flatten the nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print("Flattened List:", flat_list)

# e) List of tuples (number, square)
pairs = [(x, x**2) for x in range(1, 9)]
print("Number-Square Tuples:", pairs)