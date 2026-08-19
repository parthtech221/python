#count frequency of each element in list
def count_frequency(lst):
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency

# Example usage:
my_list = [1, 2, 2, 3, 3, 3]
freq = count_frequency(my_list)
print(freq)  # Output: {1: 1, 2: 2, 3: 3}