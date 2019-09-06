# returns missing numbers in sorted list of integers
def missingNums(min, max, array):
    returnList = []
    # gap at the beginning of list
    if array[0] > min:
        for i in range(min, array[0]):
            returnList.append(i)

    # fill gaps between numbers
    previous = min
    next = None
    for i in range(0, len(array)):
        next = array[i]
        for j in range(previous + 1, next):
            returnList.append(j)
        previous = array[i]

    # fill gaps at end of list
    if array[len(array) - 1] < max:
        for i in range(array[len(array) - 1] + 1, max + 1):
            returnList.append(i)

    return returnList


input = [2, 3, 4, 7, 8]
print(missingNums(1, 10, input))
