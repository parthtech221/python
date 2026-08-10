#count digits in a string
string = input("Enter a string: ")
digit = "1234567890"
count = 0
for char in string:
    if char in digit:
        count += 1
print("The number of digits in the string is:", count)