#Neon number
def is_neon_number(n):
    square = n * n
    sum_of_digits = sum(int(digit) for digit in str(square))
    return sum_of_digits == n

n = int(input("Enter a number: "))
print(is_neon_number(n))