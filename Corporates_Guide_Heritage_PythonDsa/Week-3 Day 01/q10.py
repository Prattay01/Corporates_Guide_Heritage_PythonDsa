# Requirement 1: Store student details (ID, Name, Course)
# Choice: Dictionary
# Why: A dictionary is ideal here because each student can be uniquely identified by their ID (as a Key), 
# which maps to a nested structure containing their name and course. This allows for constant-time lookups.
student_details = {
    1001: {"name": "Alice", "course": "Data Science"},
    1002: {"name": "Bob", "course": "Web Development"}
}


# Requirement 2: Store unique course categories
# Choice: Set
# Why: Sets inherently prevent duplicate values. This ensures that no matter how many courses are added, 
# the system will maintain an accurate, distinct list of operational categories automatically.
course_categories = {"Programming", "Design", "Marketing", "Business"}


# Requirement 3: Store course ratings for multiple courses
# Choice: Dictionary (mapping Course Name to a List of numerical ratings)
# Why: A dictionary allows us to map each specific course title to its collection of reviews. 
# A list is used for the values because we need to preserve multiple duplicate numerical ratings (e.g., several 5-star ratings) to compute averages later.
course_ratings = {
    "Python Basics": [5, 4, 5, 3, 5],
    "UI/UX Intro": [4, 4, 5, 4]
}

# Visual printout of the structure setup
print("Structures initialized successfully.")