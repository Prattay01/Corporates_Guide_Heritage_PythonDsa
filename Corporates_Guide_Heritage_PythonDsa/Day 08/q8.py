# a) Create a list of product tuples
inventory = [
    (101, "Laptop", 50000, 10),
    (102, "Mouse", 500, 3),
    (103, "Keyboard", 1200, 4),
    (104, "Monitor", 15000, 6),
    (105, "Printer", 8000, 2),
    (106, "Speaker", 2500, 8),
    (107, "Webcam", 1800, 1),
    (108, "Headphones", 3000, 7)
]

# b) Functions
def add_product(product):
    inventory.append(product)

def remove_product(name):
    global inventory
    inventory = [p for p in inventory if p[1] != name]

def update_quantity(name, qty):
    global inventory
    for i, product in enumerate(inventory):
        if product[1] == name:
            inventory[i] = (product[0], product[1], product[2], qty)

# c) Total inventory value
def total_inventory_value():
    total = 0
    for pid, name, price, quantity in inventory:
        total += price * quantity
    return total

# Add a new product
add_product((109, "Tablet", 20000, 5))

# Update quantity
update_quantity("Mouse", 10)

# Remove a product
remove_product("Webcam")

# Display inventory
print("=== INVENTORY ===")
for product in inventory:
    print(product)

# Total inventory value
print("\nTotal Inventory Value:", total_inventory_value())

# d) Low stock alert
print("\n=== LOW STOCK PRODUCTS ===")
for pid, name, price, quantity in inventory:
    if quantity < 5:
        print(name, "- Quantity:", quantity)

# e) Sort by price ascending
print("\n=== PRODUCTS SORTED BY PRICE ===")
sorted_products = sorted(inventory, key=lambda x: x[2])

for product in sorted_products:
    print(product)

# f) Search product by name
search_name = "Laptop"

print("\n=== SEARCH RESULT ===")
for product in inventory:
    if product[1].lower() == search_name.lower():
        print("Found:", product)
        break
else:
    print("Product not found")