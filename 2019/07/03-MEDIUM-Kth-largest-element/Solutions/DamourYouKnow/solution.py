# O(n^2) but I'm trying to golf this one.
def kth_largest(arr, k):
    return min([arr.pop(arr.index(max(arr))) for i in range(0,k)])
