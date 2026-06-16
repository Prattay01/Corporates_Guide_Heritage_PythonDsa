inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 30
}

print("Products:")
for product in inventory.keys():
    print(f"- {product}")

print("-" * 20)
print("Quantities:")
for qty in inventory.values():
    print(f"- {qty}")

print("-" * 20)
print("Inventory Details:")
for product, qty in inventory.items():
    print(f"{product}: {qty} units")