p=float(input("enter the principal amount: "))
r=float(input("enter the rate of interest: "))
t=float(input("enter the time period: "))
A=p*(1+r/100)**t
CI=A-p
print("the compound interest is:", CI)