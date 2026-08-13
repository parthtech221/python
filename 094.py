#string compression
string = input("Enter a string: ")
compressed = ""
current_char = string[0]
count = 1

for char in string[1:]:
    if char == current_char:
        count += 1
    else:
        compressed += current_char + str(count)
        current_char = char
        count = 1

compressed += current_char + str(count)
print("The compressed string is:", compressed)