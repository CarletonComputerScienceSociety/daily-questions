def calculate(coins, total, out=0):
    for coin in sorted(coins, reverse=True):
        out += total // coin
        total %= coin
    return -1 if total else out

print(calculate([1,2,5], 11))
print(calculate([1,5,10,25,39], 100))
print(calculate([2], 3))