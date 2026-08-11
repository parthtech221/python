#replace charcater in string
string=input("Enter a string: ")
old_char=input("Enter the character to be replaced: ")
new_char=input("Enter the new character: ")
string = string.replace(old_char, new_char)
print("The string after replacing the character is:", string)