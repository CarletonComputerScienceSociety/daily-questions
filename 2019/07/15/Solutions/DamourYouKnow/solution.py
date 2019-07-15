def count_jewels(jewels, stones):
    return len([s for s in stones if s in set(jewels)])

print(count_jewels('aA', 'aAAbbbb'))
print(count_jewels('z', 'ZZ'))