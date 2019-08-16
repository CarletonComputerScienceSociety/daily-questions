def pazaak(h1, h2):
    h1_sum, h2_sum = sum(h1), sum(h2)
    if h1_sum <= 20 and h2_sum <= 20:
        return max([h1_sum, h2_sum]) if h1_sum != h2_sum else None
    if h1_sum and h2_sum > 20:
        return None
    return h1_sum if h1_sum <= 20 else h2_sum

print(pazaak([5, 10, 4], [6, 6, 1, 2, 3])) # 19
print(pazaak([9, 9, 4, -2], [10, 10])) # None
print(pazaak([9, 8, 4], [5, 6, 4])) # 15