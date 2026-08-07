#perfect number
def is_perfect(n):
    if n <= 1:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

n=int(input("Enter a number: "))
print(is_perfect(n)) 