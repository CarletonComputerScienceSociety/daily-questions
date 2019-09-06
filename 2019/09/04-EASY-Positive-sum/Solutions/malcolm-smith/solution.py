def sumOfMagnitude(array):
    sum = 0
    for i in array:
        if i < 0:
            sum += i * -1
        else:
            sum += i
    return sum

print(sumOfMagnitude([5, -3, 2, -1]))