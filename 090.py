#find longest word in a string
string = input("Enter a string: ")
words = string.split()
longest_word = max(words, key=len)
print("The longest word in the string is:", longest_word)