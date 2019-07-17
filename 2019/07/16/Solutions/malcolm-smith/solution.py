def separateEvenOdd(a):
    return [i for i in a if ((i % 2) == 0)] + [i for i in a if ((i % 2) != 0)]

print(separateEvenOdd([ 3, 1, 2, 4 ]))
