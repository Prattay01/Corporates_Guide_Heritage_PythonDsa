# --- Part A: Number Statistics ---
count = 0
total_sum = 0
maximum = None
minimum = None

while True:
    n = int(input("Enter an integer (0 to stop): "))
    if n == 0:
        break
    count += 1
    total_sum += n
    if maximum is None or n > maximum:
        maximum = n
    if minimum is None or n < minimum:
        minimum = n

if count > 0:
    print(f"Count: {count} | Sum: {total_sum} | Max: {maximum} | Min: {minimum}")
else:
    print("No numbers were entered.")

# --- Part B: Prime Numbers (1 to 100) ---
prime_count = 0
print("\nPrime numbers between 1 and 100:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        prime_count += 1
print(f"\nTotal prime numbers: {prime_count}")

# --- Part C: Reverse a Number ---
num = int(input("\nEnter a number to reverse: "))
is_negative = num < 0
num = abs(num)
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

if is_negative:
    reversed_num = -reversed_num
print(f"Reversed number: {reversed_num}")