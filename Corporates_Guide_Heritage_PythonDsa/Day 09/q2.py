# ===== Question 2 =====
print("\n===== Question 2 =====")

inventory = {
    'apple': 50,
    'banana': 30,
    'mango': 0,
    'cherry': 15,
    'grape': 0
}

print("Inventory:")
print(inventory)

# a) Print all product names using keys()

print("\nProduct Names:")
print(list(inventory.keys()))

# b) Print all quantities using values()

print("\nQuantities:")
print(list(inventory.values()))

# c) Print items using items()

print("\nInventory Details:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity} units")

# d) Check quantity of papaya safely

print("\nPapaya Quantity:")
print(inventory.get("papaya", "Not available"))

# e) Remove mango and print popped value

removed = inventory.pop("mango")
print("\nRemoved Item Quantity:")
print(removed)

print("Inventory After Removing Mango:")
print(inventory)

# f) Add 3 new products using update()

inventory.update({
    "orange": 20,
    "kiwi": 12,
    "pear": 18
})

print("\nInventory After Update:")
print(inventory)

# g) Add watermelon only if it doesn't exist

inventory.setdefault("watermelon", 25)

print("\nInventory After setdefault():")
print(inventory)

# h) Print out-of-stock items

print("\nOut of Stock Products:")
for product, quantity in inventory.items():
    if quantity == 0:
        print(f"{product}: {quantity} units")