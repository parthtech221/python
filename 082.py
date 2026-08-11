#palindrome string
string = input("Enter a string: ")
cleaned_string = ''.join(c.lower() for c in string if c.isalnum())
is_palindrome = cleaned_string == cleaned_string[::-1]
print("Is the string a palindrome?", is_palindrome)