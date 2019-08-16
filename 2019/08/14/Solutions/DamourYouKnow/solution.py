def mode(arr):
    if not arr:
        return set()
    counts = {}
    for num in arr:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    maximum = max(counts.values())
    return {num for num in arr if counts[num] == maximum}


print(mode([])) # {}
print(mode([1,2,3,3,4])) # {3} 
print(mode([1,2,3,4,3,4])) # {3,4}