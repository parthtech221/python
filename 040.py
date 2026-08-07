n=int(input("enter a number: "))
for i in range(n):
    prime=True
    for j in range(2,i):
        if i%j==0:
            prime=False
            break
    if prime :
        print(i)
       

        