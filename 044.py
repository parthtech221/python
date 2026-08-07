#armstrong number
def is_armstrong_number(n):
    original_number = n
    num_digits = len(str(n))
    sum_of_powers = 0

    while n > 0:
        digit = n % 10
        sum_of_powers += digit ** num_digits
        n //= 10

    return sum_of_powers == original_number

n = int(input("Enter a number: "))
print(is_armstrong_number(n))