#bubble sort
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

my_list = [1, 2, 3, 6, 4, 9, 5]
filtered_list = bubble_sort(my_list)
print(filtered_list) 