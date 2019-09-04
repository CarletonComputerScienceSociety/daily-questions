def chunks(arr, k):
    return [arr[x:x+k] for x in range(0, len(arr), k)]
