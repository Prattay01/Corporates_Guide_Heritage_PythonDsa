# Loop through numbers 1 to 100 inclusive
for i in range(1, 101):
    # Initialize an empty string buffer for the current number
    output = ""
    
    # 1. Evaluate individual rule conditions sequentially
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if i % 7 == 0:
        output += "Bang"
        
    # 2. Output determination fallback phase
    if output == "":
        # If no conditions matched, print the original number
        print(i)
    else:
        # If any strings were collected, print the combined result
        print(output)