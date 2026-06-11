# ===== Question 1 =====
print("\n===== Question 1 =====")
# a) Create a dictionary called 'student'
student = {
    "name": "Prattay",
    "age": 21,
    "course": "B.Tech CSE",
    "city": "Kolkata",
    "gpa": 8.5
}

print("Initial Dictionary:")
print(student)

# b) Access and print each value using [] and get()

print("\nUsing [] notation:")
print(student["name"])
print(student["age"])
print(student["course"])
print(student["city"])
print(student["gpa"])

print("\nUsing get() method:")
print(student.get("name"))
print(student.get("age"))
print(student.get("course"))
print(student.get("city"))
print(student.get("gpa"))

# c) Add email and phone

student["email"] = "prattay@example.com"
student["phone"] = "2345824567"

print("\nAfter adding email and phone:")
print(student)

# d) Update GPA and delete city

student["gpa"] = 8.9
del student["city"]

print("\nAfter updating GPA and deleting city:")
print(student)

# e) Check keys using in

print("\nKey Checks:")
print("name" in student)
print("address" in student)

# f) Total key-value pairs

print("\nTotal key-value pairs:")
print(len(student))