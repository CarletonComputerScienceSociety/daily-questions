def rotateRight(a, k):
    k = k % len(a) # this will shorten complexity if k > len(a)
    return (a[-k:] + a[:-k])

print(rotateRight([1, 2, 3, 4, 5, 6, 7], 3))
