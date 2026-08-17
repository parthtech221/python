a=[42, 7, 89, 42, 15, 63, 77, 28, 94, 56, 3, 77, 3]
b=[]
for i in a:
    if i not in b:
        b.append(i)

print(b)        