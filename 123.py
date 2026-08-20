def move_zeros(arr):
    result = []

    for num in arr:
        if num != 0:
            result.append(num)

    zero_count = len(arr) - len(result)

    for i in range(zero_count):
        result.append(0)

    return result


arr = [1, 0, 2, 0, 3, 4, 0]
print(move_zeros(arr))
