#password strength checker
password = input("Enter a password: ")

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.")
else:
    print("Password is strong.")