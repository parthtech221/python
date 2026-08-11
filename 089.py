#reverse each word in a string
string = input("Enter a string: ")
words = string.split()
reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)
print("The string with reversed words is:", result)