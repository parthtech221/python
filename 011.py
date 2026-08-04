second=int(input("Enter the number of seconds: "))
hours=second//3600
minutes=(second%3600)//60
seconds=second%60
print(f"{hours}:{minutes}:{seconds}")
