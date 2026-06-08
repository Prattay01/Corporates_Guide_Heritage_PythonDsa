marks = float(input("Enter the marks obtained (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid input! Marks must be between 0 and 100.")
else:
    # Everything inside this else block must be indented by an extra 4 spaces
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B+"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"Marks: {marks} | Final Grade: {grade}")