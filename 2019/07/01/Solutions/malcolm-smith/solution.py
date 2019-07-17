def maxValue(arr):
    max = 0
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]
    return max


print(maxValue([1, 4, 2, 7, 10, 8]))
