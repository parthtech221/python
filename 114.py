#rotate list
def rotate_list(lst, n):
    return lst[n:] + lst[:n]

# Example usage:
my_list = [1, 2, 3, 4, 5]
rotated_list = rotate_list(my_list, 2)
print(rotated_list)  # Output: [3, 4, 5, 1, 2]