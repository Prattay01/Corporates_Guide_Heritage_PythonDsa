raw_name = "   Arjun Mehta   "
raw_id = "00542"
raw_base_salary = "85000"
raw_allowance = "12500.75"
raw_active_status = "Yes"
name = raw_name.strip()

employee_id = int(raw_id)
total_salary = float(raw_base_salary) + float(raw_allowance)

department = "Information Technology"

is_active = raw_active_status.strip().lower() == "yes"
print("=" * 43)
print(f"{'CORPORATE ERP SYSTEM: PROFILE REPORT':^43}")
print("=" * 43)
print(f"{'Field':<18} | {'Value':<22}")
print("-" * 43)
print(f"{'Employee Name':<18} | {name:<22}")
print(f"{'System ID':<18} | {employee_id:0>6}")  
print(f"{'Department':<18} | {department:<22}")
print(f"{'Gross Salary':<18} | ${total_salary:,.2f}")  
print(f"{'Active Status':<18} | {str(is_active):<22}")

print("=" * 43)