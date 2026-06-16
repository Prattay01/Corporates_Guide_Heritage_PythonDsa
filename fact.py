def factorial(n):
    if n == 0 or n == 1:   # Base Case
        return 1

    return n * factorial(n - 1)   # Recursive Case

print(factorial(5))