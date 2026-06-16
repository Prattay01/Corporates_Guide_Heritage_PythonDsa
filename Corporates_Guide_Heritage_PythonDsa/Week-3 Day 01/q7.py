library_A = {"Rahul", "Amit", "Priya", "Sneha"}
library_B = {"Priya", "Karan", "Amit", "Vikram"}

# 1. Members present in both libraries
both_libraries = library_A.intersection(library_B)
print("Members in both libraries:", both_libraries)

# 2. Members present in either library
either_library = library_A.union(library_B)
print("Members in either library:", either_library)

# 3. Members only in Library A
only_library_A = library_A.difference(library_B)
print("Members only in Library A:", only_library_A)