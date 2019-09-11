def isEvilNumber(n):
    count = 0
    for char in str(bin(n)[2:]):
        if char == '1':
            count += 1
    if count % 2 == 0:
        return True
    else:
        return False


print(isEvilNumber(4))