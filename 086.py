#Find first occurrence of a character in a string
string = input("Enter a string: ")
char = input("Enter the character to find: ")
index = string.find(char)
if index != -1:
    print(f"The first occurrence of '{char}' is at index {index}.")
else:
    print(f"The character '{char}' is not found in the string.")