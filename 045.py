#harshad number
def is_harshad_number(n):
    original_number = n
    sum_of_digits = sum(int(digit) for digit in str(n))
    return original_number % sum_of_digits == 0

n = int(input("Enter a number: "))
print(is_harshad_number(n))