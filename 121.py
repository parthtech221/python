def linear(lst,target):
    n=len(lst)
    for i in range(n):
        if lst[i]==target:
            return i
    return "not found"  
a=[1, 2, 3, 4, 5]
search=linear(a,6)
print(search)
    