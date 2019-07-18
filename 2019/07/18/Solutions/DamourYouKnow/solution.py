def merge_intervals(intervals):
    if not intervals:
        return []

    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        merged = merged[:-1] + merge(merged[-1], intervals[i])
    return merged

def merge(a, b):
    return [[a[0], b[1]]] if a[1] >= b[0] else [a, b]

print(merge_intervals([[1,3],[2,6],[6,10],[15,18]]))
print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[1,3]]))
print(merge_intervals([]))