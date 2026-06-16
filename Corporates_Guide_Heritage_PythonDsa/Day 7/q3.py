def factorial(n):
    if n < 0:
        return "Error: Factorial is undefined for negative numbers."
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n <= 0:
        print("Error: Number of terms must be a positive integer greater than 0.")
        return
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()


if __name__ == "__main__":
    print(factorial(5))
    fibonacci(7)