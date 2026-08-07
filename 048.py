#spy number

def is_spy_number(n):
    digits = [int(digit) for digit in str(n)]
    sum_of_digits = sum(digits)
    product_of_digits = 1
    for digit in digits:
        product_of_digits *= digit
    return sum_of_digits == product_of_digits

n = int(input("Enter a number: "))
print(is_spy_number(n))