def fewest_coins(coins, amount):
    # Sorting the coins from highest to lowest
    coins.sort(reverse=True)

    coin_count = 0
    # For each coin
    for coin in coins:
        # Getting how many of the current coin we have
        curr_coin_count = amount // coin

        # Incrementing how many total coins we have
        coin_count += curr_coin_count

        # Subtracting their value from the amount
        amount -= coin * curr_coin_count

        # If we have found the total amount
        if not amount:
            return coin_count
    return -1
