def selection_sort(lst):
    n=len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

my_list = [10, 2, 3, 6, 4, 9, 5]
filtered_list = selection_sort(my_list)
print(filtered_list)             