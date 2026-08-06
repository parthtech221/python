a=int(input("Enter a number: "))
count=0

while a>0:
    digit=a%10
    a//=10
    if digit%2!=0:
        count+=1
    
print(f"The number of odd digits in the number is {count}.")    