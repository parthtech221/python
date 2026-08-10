#count consonants in a string
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char not in vowels:
        count += 1
print("The number of consonants in the string is:", count)