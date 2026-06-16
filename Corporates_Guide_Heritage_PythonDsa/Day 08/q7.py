# a) List of 10 student records
students = [
    ("Alice", 101, [85, 90, 88, 92, 87]),
    ("Bob", 102, [70, 75, 72, 68, 74]),
    ("Charlie", 103, [95, 98, 96, 94, 97]),
    ("Diana", 104, [80, 82, 78, 85, 81]),
    ("Ethan", 105, [60, 65, 62, 58, 64]),
    ("Fiona", 106, [88, 86, 90, 89, 87]),
    ("George", 107, [73, 76, 74, 72, 75]),
    ("Hannah", 108, [91, 93, 89, 92, 90]),
    ("Ian", 109, [55, 60, 58, 57, 59]),
    ("Julia", 110, [84, 86, 82, 85, 83])
]

# b) Function to calculate average
def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

# c) Create (name, average_score) list using list comprehension
averages = [
    (name, calculate_average(marks))
    for name, roll, marks in students
]

# d) Sort by average score (descending)
averages.sort(key=lambda x: x[1], reverse=True)

print("===== CLASS RANK =====")
for rank, (name, avg) in enumerate(averages, start=1):
    print(f"{rank}. {name} - {avg:.2f}")

# e) Count students above 75 average
above_75 = len([avg for name, avg in averages if avg > 75])

print("\nStudents above 75 average:", above_75)

# f) Topper and lowest scorer
topper = averages[0]
lowest = averages[-1]

print("\nTopper:")
print(f"{topper[0]} - {topper[1]:.2f}")

print("\nLowest Scorer:")
print(f"{lowest[0]} - {lowest[1]:.2f}")