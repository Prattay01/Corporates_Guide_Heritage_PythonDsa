# a) Create a tuple called 'months'
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# b) Access and print elements
print("3rd month:", months[2])
print("Last month:", months[-1])
print("Months from index 3 to 6:", months[3:7])

# c) Try to change the first element
try:
    months[0] = "January_New"
except TypeError as e:
    print("Error:", e)

# d) Single-element tuple containing your name
name = ("Prattay",)
print("Name Tuple:", name)
print("Type:", type(name))

# e) Convert tuple to list, add a 13th month, then convert back
months_list = list(months)
months_list.append("Intercalary")

months = tuple(months_list)
print("Updated Tuple:", months)