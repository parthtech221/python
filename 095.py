#check string rotation
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) == len(string2):
    if string1 in string2 + string2:
        print("The strings are rotations of each other.")
    else:
        print("The strings are not rotations of each other.")
else:
    print("The strings are not rotations of each other.")