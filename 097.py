#check pangram
string = input("Enter a string: ")
string = string.replace(" ", "").lower()
if len(set(string)) == 26:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")