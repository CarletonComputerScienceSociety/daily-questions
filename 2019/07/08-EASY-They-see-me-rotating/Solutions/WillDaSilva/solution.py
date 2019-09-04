from collections import deque

def rotate_list(x, k):
    x = deque(x)
    x.rotate(k)
    return x
