#movie ticket pricing system
age = int(input("Enter your age: "))

if age < 13:
    print("Child tickets are $10.")
elif age >= 13 and age <= 17:
    print("Teenage tickets are $15.")
else:
    print("Adult tickets are $20.")