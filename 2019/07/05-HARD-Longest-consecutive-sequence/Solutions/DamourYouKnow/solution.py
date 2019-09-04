def longest_sequence(arr):
    arr_set = set(arr)
    counts = []
    for num in arr:
        higher, lower = 0, 0
        while num + higher + 1 in arr_set: higher += 1
        while num - lower - 1 in arr_set: lower += 1
        counts.append(higher + lower + 1)
        arr_set -= {n for n in range(num - lower, num + higher + 1)}
    return max(counts)


print(longest_sequence([100, 4, 200, 1, 3, 2]))