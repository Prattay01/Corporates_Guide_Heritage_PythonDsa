student_marks = {
    "Rahul": 85,
    "Amit": 78,
    "Priya": 92,
    "Sneha": 88,
    "Karan": 69
}

names = list(student_marks.keys())
print("Student Names:", names)
print("Marks:", list(student_marks.values()))
total_marks = sum(student_marks.values())
num_students = len(student_marks)
average_mark = total_marks / num_students

print(f"Average Marks: {average_mark:.1f}")