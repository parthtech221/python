#product of first n number
n = int(input("Enter a number: "))
product = 1
for i in range(1, n + 1):
    product *= i
print(f"The product of the first {n} numbers is {product}.")
