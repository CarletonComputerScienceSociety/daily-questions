import heapq

def kth_largest(x, k):
    heapq.heapify(x)
    return heapq.nlargest(k, x)[-1]

