#count special characters in a string
string = input("Enter a string: ")
special_characters = "!@#$%^&*()_+-=[]{}|;':\",.<>/?`~"
count = 0
for char in string:
    if char in special_characters:
        count += 1
print("The number of special characters in the string is:", count)        