#palindrome number pattern
for i in range(5):
    for j in range(5-i):
        print(" ", end=" ")
    for k in range(i+1):
        print(k+1, end="")
    for l in range(i-1,-1,-1):
        print(l+1, end="")
    print()