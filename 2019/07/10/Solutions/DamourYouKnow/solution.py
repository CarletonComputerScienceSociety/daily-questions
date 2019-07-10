def change(coins, amount):
    total_count = 0
    for coin in sorted(coins, reverse=True):
        total_count += amount // coin
        amount -= (amount // coin) * coin
    return total_count if amount == 0 else -1

        
print(change([1,2,5], 11))
print(change([1,5,10,25,39], 100))
print(change([2], 3))
