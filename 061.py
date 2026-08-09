#sandglass pattern 
for i in range(5):
    for j in range(i):
        print(" ", end=" ")
    for k in range(2*(5-i)-1):
        print("*", end=" ")
    print()
for i in range(3, -1, -1):
    for j in range(i):
        print(" ", end=" ")
    for k in range(2*(5-i)-1):
        print("*", end=" ")
    print()