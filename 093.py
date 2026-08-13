#character frequency counter
string = input("Enter a string: ")
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print("Character frequencies:")
for char, freq in frequency.items():
    print(f"'{char}': {freq}")