import math


def is_happy(x):
    if x == 1:
        return True

    count = 0
    curr_ten = 1

    try:
        for curr_ten in range(0, int(math.ceil(math.log10(x)))):
            count += ((x // (10**curr_ten)) % 10)**2
    except ValueError:
        return True

    return is_happy(count)
