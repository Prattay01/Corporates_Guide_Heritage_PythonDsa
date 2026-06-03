name = "Arjun Mehta"
employee_id = 10452
department = "Information Technology"
salary = 125500.756 
report_string = (
    f"=== EMPLOYEE PROFILE REPORT ===\n"
    f"ID          : {employee_id}\n"
    f"Name        : {name}\n"
    f"Department  : {department}\n"
    f"Monthly Net : ${salary:,.2f}\n"
)

print(report_string)
