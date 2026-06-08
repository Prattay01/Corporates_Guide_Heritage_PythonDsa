age = int(input("Enter the age of the ticket holder: "))
group_size = int(input("Enter the total number of people in your group: "))

if age >= 18:
    if age >= 60:
        base_price = 100  # Senior rate
    else:
        base_price = 200  # Standard Adult rate
else:
    if age < 5:
        base_price = 0    # Free entry for toddlers
    else:
        base_price = 80   # Standard Child rate

gross_total = base_price * group_size
if group_size > 10:
    discount = gross_total * 0.20
    final_total = gross_total - discount
    discount_applied = True
else:
    discount = 0.0
    final_total = gross_total
    discount_applied = False
print("..................................................................")
print(f"Base Ticket Price : {base_price} INR")
print(f"Group Size        : {group_size}")
print(f"Gross Subtotal    : {gross_total} INR")
if discount_applied:
    print(f"Group Discount(20%): -{discount:.2f} INR")
print(f"Final Total Bill  : {final_total:.2f} INR")
