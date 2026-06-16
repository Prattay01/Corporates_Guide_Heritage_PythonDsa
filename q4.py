def factorial(n):
    # Base case: 0! and 1! are both 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: n * (n - 1)!
    return n * factorial(n - 1)


def sum_of_digits(n):
    # Base case: If the number is a single digit, just return it
    if n < 10:
        return n
    
    # Recursive case: Last digit + sum of the remaining digits
    # (n % 10) gets the last digit, (n // 10) removes the last digit
    return (n % 10) + sum_of_digits(n // 10)


# --- Testing Both Functions ---

# 1. Test Factorial
fact_input = 5
fact_result = factorial(fact_input)
print(f"Factorial of {fact_input}: {fact_result}")  # Output: 120

# 2. Test Sum of Digits
digits_input = 1234
digits_result = sum_of_digits(digits_input)
print(f"Sum of digits for {digits_input}: {digits_result}")  # Output: 10