def count_jewels(jewels, stones):
    return sum(stone in set(jewels) for stone in stones)

