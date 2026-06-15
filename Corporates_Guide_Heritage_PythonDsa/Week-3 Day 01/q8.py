shopping_cart = {
    "Wireless Mouse": 25.00,
    "Mechanical Keyboard": 85.50
}
print("Initial Cart:", shopping_cart)

# 1. Add a new product
shopping_cart["USB-C Cable"] = 12.99

# 2. Update the price of an existing product
shopping_cart["Wireless Mouse"] = 22.00

# 3. Remove a product
shopping_cart.pop("Mechanical Keyboard")

print("Updated Cart:", shopping_cart)

# 4. Calculate total cart value
total_value = sum(shopping_cart.values())
print(f"Total Cart Value: ${total_value:.2f}")