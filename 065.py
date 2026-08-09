#prime number pattern
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
print("Prime number pattern:")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        if is_prime(k):
            print(k, end=" ")
        else:
            print(" ", end=" ")
    print()