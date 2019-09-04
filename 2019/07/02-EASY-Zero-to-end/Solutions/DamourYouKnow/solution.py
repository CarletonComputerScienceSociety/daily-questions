def zeroes_to_end(arr):
    return [num for num in arr if num != 0] + [num for num in arr if num == 0]
