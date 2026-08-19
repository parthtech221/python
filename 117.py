#remove all occurrences of an element 
def remove_occurrences(lst, element):
    return [x for x in lst if x != element]

# Example usage:
my_list = [1, 2, 3, 2, 4, 2, 5]
filtered_list = remove_occurrences(my_list, 2)
print(filtered_list)  # Output: [1, 3, 4, 5]