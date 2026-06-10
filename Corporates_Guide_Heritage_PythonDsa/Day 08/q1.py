# a) Create a list called student_marks with 10 integer values
student_marks = [78, 85, 92, 67, 88, 74, 95, 81, 69, 100]

# b) Print the first 3 elements, last 3 elements, and every alternate element
print("First 3 elements:", student_marks[:3])
print("Last 3 elements:", student_marks[-3:])
print("Every alternate element:", student_marks[::2])

# c) Print the total number of elements
print("Total number of elements:", len(student_marks))

# d) Update the 5th element to 95 and print the updated list
student_marks[4] = 95
print("Updated list:", student_marks)

# e) Print the list in reverse order using slicing
print("Reversed list:", student_marks[::-1])