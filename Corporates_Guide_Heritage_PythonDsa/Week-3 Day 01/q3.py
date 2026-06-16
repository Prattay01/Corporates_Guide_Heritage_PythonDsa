employees = {
    "E101": "Rahul Sharma",
    "E102": "Priya Patel",
    "E103": "Amit Verma"
}
search_id = input("Enter Employee ID to search: ").strip()
result = employees.get(search_id, "Employee Not Found")

print(result)