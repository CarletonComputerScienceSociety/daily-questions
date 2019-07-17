def fewest_coins_needed(coins, amount, used=0):
    for coin in sorted(coins, reverse=True):
        coins_used, amount = divmod(amount, coin)
        used += coins_used
    return used if amount == 0 else -1

