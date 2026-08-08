#hollow pyramid pattern
for i in range(5):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(2*i+1):
        if k==0 or k==2*i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()