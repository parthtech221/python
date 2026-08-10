#count space in string
string = input("Enter a string: ")
count = 0
for char in string:
    if char == " ":
        count += 1
print("The number of spaces in the string is:", count)
