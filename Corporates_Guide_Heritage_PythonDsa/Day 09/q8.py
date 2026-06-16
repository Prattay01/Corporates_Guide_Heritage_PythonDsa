# ===== Challenge 1 =====

print("\n===== Challenge 1 =====")

# a) Store at least 10 student records

students = [
    {"name": "Aman", "roll": 1, "subjects": {"Math": 88, "Science": 76, "English": 90}},
    {"name": "Riya", "roll": 2, "subjects": {"Math": 92, "Science": 85, "English": 78}},
    {"name": "Rahul", "roll": 3, "subjects": {"Math": 45, "Science": 52, "English": 60}},
    {"name": "Neha", "roll": 4, "subjects": {"Math": 70, "Science": 65, "English": 72}},
    {"name": "Arjun", "roll": 5, "subjects": {"Math": 55, "Science": 90, "English": 82}},
    {"name": "Priya", "roll": 6, "subjects": {"Math": 98, "Science": 95, "English": 91}},
    {"name": "Ishita", "roll": 7, "subjects": {"Math": 80, "Science": 75, "English": 88}},
    {"name": "Karan", "roll": 8, "subjects": {"Math": 60, "Science": 67, "English": 70}},
    {"name": "Meera", "roll": 9, "subjects": {"Math": 86, "Science": 89, "English": 92}},
    {"name": "Dev", "roll": 10, "subjects": {"Math": 40, "Science": 42, "English": 44}}
]

# b) Function to calculate average marks

def get_average(student):
    marks = student["subjects"].values()
    return sum(marks) / len(marks)

print("\nStudent Averages:")

for student in students:
    print(f"{student['name']} -> {get_average(student):.2f}")

# c) Students who passed all subjects

passed_students = []

for student in students:
    if all(mark >= 40 for mark in student["subjects"].values()):
        passed_students.append(student["name"])

print("\nStudents Who Passed All Subjects:")
print(passed_students)

# d) Subjects where at least one student scored below 50

low_score_subjects = set()

for student in students:
    for subject, mark in student["subjects"].items():
        if mark < 50:
            low_score_subjects.add(subject)

print("\nSubjects Having At Least One Score Below 50:")
print(low_score_subjects)

# e) Dictionary of subject-wise scores

subject_scores = {}

for student in students:
    for subject, mark in student["subjects"].items():
        subject_scores.setdefault(subject, []).append(mark)

print("\nSubject Wise Scores:")

for subject, scores in subject_scores.items():
    print(f"{subject}: {scores}")

print("\nClass Average Per Subject:")

for subject, scores in subject_scores.items():
    average = sum(scores) / len(scores)
    print(f"{subject}: {average:.2f}")

# f) Find topper and rank all students

ranked_students = sorted(
    students,
    key=get_average,
    reverse=True
)

print("\nTopper:")
print(
    f"{ranked_students[0]['name']} "
    f"with average {get_average(ranked_students[0]):.2f}"
)

print("\nStudent Rankings:")

for rank, student in enumerate(ranked_students, start=1):
    print(
        f"{rank}. {student['name']} "
        f"({get_average(student):.2f})"
    )

# g) Subjects taken by ALL students

common_subjects = set(students[0]["subjects"].keys())

for student in students[1:]:
    common_subjects = common_subjects.intersection(
        set(student["subjects"].keys())
    )

print("\nSubjects Taken By All Students:")
print(common_subjects)

