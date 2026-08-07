#Automorphic number
def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

n = int(input("Enter a number: "))
print(is_automorphic(n))