#check isomorphic strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if len(string1) == len(string2):
    mapping = {}
    reverse_mapping = {}
    is_isomorphic = True

    for i in range(len(string1)):
        char1 = string1[i]
        char2 = string2[i]

        if char1 in mapping:
            if mapping[char1] != char2:
                is_isomorphic = False
                break
        else:
            mapping[char1] = char2

        if char2 in reverse_mapping:
            if reverse_mapping[char2] != char1:
                is_isomorphic = False
                break
        else:
            reverse_mapping[char2] = char1

    if is_isomorphic:
        print("The strings are isomorphic.")
    else:
        print("The strings are not isomorphic.")
else:
    print("The strings are not isomorphic.")