def count_jewels(jewels, stones):
    stone_dict = {}
    for stone in stones:
        if stone_dict.get(stone):
            stone_dict[stone] += 1
        else:
            stone_dict[stone] = 1

    jewel_count = 0
    for jewel in jewels:
        if stone_dict.get(jewel):
            jewel_count += stone_dict[jewel]

    return jewel_count