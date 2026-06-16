employees = [
    (452, "rohit singh"),
    (1089, "riya Sharma"),
    (12405, "Prattay Bari")
]

print(f"{'Employee Name':<20} | {'ID':>6}")
print("-" * 29)
for emp_id, name in employees:
    print(f"{name:<20} | {emp_id:0>6}")