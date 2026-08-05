a=float(input("enter a number:"))
if a<10:
    print(a)
else:
    while a>=10:
        a//=10
    print(a)   