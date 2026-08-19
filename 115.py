#split into even and odd
def split_even_odd(lst):
    even = [x for x in lst if x % 2 == 0]
    odd = [x for x in lst if x % 2 != 0]
    return even, odd

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers, odd_numbers = split_even_odd(my_list)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)