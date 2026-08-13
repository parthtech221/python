#find shortest word in a string
string = input("Enter a string: ")
words = string.split()
shortest_word = min(words, key=len)
print("The shortest word in the string is:", shortest_word)