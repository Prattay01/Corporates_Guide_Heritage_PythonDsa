# Shopping Bill Generator

p_name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: "))

total_cost = quantity * price
gst = total_cost * 0.18
final_bill = total_cost + gst

print("Bill Details........................")
print("Product:", p_name)
print("Quantity:", quantity)
print("Price per Unit:", price)
print("Total Cost:", total_cost)
print("GST (18%):", gst)
print("Final Bill:", final_bill)