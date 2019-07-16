def separateEvenOdd(a):
    arr = [i for i in a if ((i % 2) == 0)] + [i for i in a if ((i % 2) != 0)]
    return arr

print(separateEvenOdd([ 3, 1, 2, 4 ]))
