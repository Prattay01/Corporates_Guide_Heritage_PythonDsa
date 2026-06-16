a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("\n--- Triangle Analysis ---")
    print("Status: Valid Triangle")
    
    if a == b == c:
        side_type = "Equilateral"
    elif (a == b) or (b == c) or (a == c):
        side_type = "Isosceles"
    else:
        side_type = "Scalene"
    
    print(f"Classification by Sides: {side_type}")
    sq_a, sq_b, sq_c = a**2, b**2, c**2
    
    if (sq_a + sq_b == sq_c) or (sq_a + sq_c == sq_b) or (sq_b + sq_c == sq_a):
        print("Classification by Angle: Right-angled Triangle 📐")
    else:
        print("Classification by Angle: Not a Right-angled Triangle")

else:
    print("\nStatus: Invalid Triangle!")
    print("Reason: The sum of any two sides must be strictly greater than the third side.")