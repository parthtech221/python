#armstrong number pattern
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == n
print("Armstrong number pattern:")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        if is_armstrong(k):
            print(k, end=" ")
        else:
            print(" ", end=" ")
    print()