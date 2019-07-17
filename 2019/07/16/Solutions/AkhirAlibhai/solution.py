def evens_odds(array):
    even_count = 0
    odd_count = len(array) - 1
    even_odd_list = [None] * len(array)

    for element in array:
        if element % 2:
            even_odd_list[odd_count] = element
            odd_count -= 1
        else:
            even_odd_list[even_count] = element
            even_count += 1

    return even_odd_list