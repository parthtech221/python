def insertion_sort(lst):
    n = len(lst)

    for i in range(1, n):
        key = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

    return lst


my_list = [10, 2, 3, 6, 4, 9, 5]
sorted_list = insertion_sort(my_list)

print(sorted_list)