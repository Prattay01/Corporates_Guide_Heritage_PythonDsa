user_input = input("Enter a number to evaluate: ")
num = float(user_input)

if num > 0:
    print(f"The number {num} is Positive.")
elif num < 0:
    print(f"The number {num} is Negative.")
else:
    print("The number is Zero.")