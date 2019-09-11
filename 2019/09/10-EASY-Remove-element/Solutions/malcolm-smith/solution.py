def removeElement(array, target):
    newArray = array[:]
    for i in range(len(newArray) - 1, -1, -1):
        if newArray[i] == target:
            del newArray[i]
    return newArray


array = [1, 2, 3, 1, 2, 3]
target = 1
array2 = ['a', 'b', 'c', 'd']
target2 = 'c'

print(removeElement(array, target))
print(removeElement(array2, target2))
