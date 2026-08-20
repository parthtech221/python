def find_pair(arr, target):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return (arr[i], arr[j])

    return "Pair Not Found"


arr = [2, 7, 11, 15]
target = 9

print(find_pair(arr, target))