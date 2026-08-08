#pascal triangle pattern
import math


for i in range(20):
    for j in range(20-i):
        print(" ", end=" ")
    for k in range(i+1):
        print(f"{math.factorial(i)//(math.factorial(k)*math.factorial(i-k))}", end="   ")
    print()