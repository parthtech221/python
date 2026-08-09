#perfect number pattern
def is_perfect(n):
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

print("Perfect number pattern:")
for i in range(1, 10):
    for j in range(10 - i):
        print("", end="")
    for k in range(1, i + 1):
        if is_perfect(k):
            print(k, end="")
        else:
            print("", end="")
    print()