#storng number

def is_strong_number(n):
    original_number = n
    sum_of_factorials = 0

    while n > 0:
        digit = n % 10
        factorial = 1
        for i in range(1, digit + 1):
            factorial *= i
        sum_of_factorials += factorial
        n //= 10

    return sum_of_factorials == original_number

n = int(input("Enter a number: "))
print(is_strong_number(n))