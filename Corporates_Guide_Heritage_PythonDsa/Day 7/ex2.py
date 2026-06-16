student = {'name': 'Alice', 'age': 22, 'grade': 'A'}

# Keys only (default)
for key in student:
    print(key)

# Keys and values
for key, value in student.items():
    print(f'{key}: {value}')

# Values only
for value in student.values():
    print(value)
