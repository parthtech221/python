#product of digit
a=int(input("Enter a number: "))
product=1
while a>0:
    digit=a%10
    product*=digit
    a//=10
print(f"The product of the digits in the number is {product}.")