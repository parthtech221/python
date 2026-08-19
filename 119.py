def selection_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(n):
            if lst[i]<lst[j]:
                lst[j], lst[i] = lst[i], lst[j]
    return lst

my_list = [10, 2, 3, 6, 4, 9, 5]
filtered_list = selection_sort(my_list)
print(filtered_list)             