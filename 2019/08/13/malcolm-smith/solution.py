input = [[1, 2, 3], [4, 5], [6], [], [7, 8, 9, 10]]

def meshArrays(arrays):
    new = []
    for array in arrays: new += array
    return new

print(meshArrays(input))