# 1. Take numerical input from the user
n = int(input("Enter the number for the multiplication table: "))

print(f"\n--- Multiplication Table for {n} ---")

# 2. Loop through multipliers from 1 to 12
for i in range(1, 13):
    # Using :2d ensures the multiplier takes up exactly 2 spaces (right-aligned)
    print(f"{n} x {i:>2d} = {n * i:>2d}")