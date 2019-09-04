input = [
    [[5, 10, 4], [6, 6, 1, 2, 3]],
    [[9, 9, 4, -2], [10, 10]],
    [[9, 8, 4], [5, 6, 4]]
]

def winningHand(hands):
    score1 = sum(hands[0])
    score2 = sum(hands[1])
    if score1 > 20: score1 = 0
    elif score2 > 20: score2 = 0
    winningScore = None
    if score1 == score2:
        return winningScore
    else:
        if score1 > score2:
            winningScore = score1
        else:
            winningScore = score2
        return ('%d (hand1 = %d, hand2 = %d)' % (winningScore, score1, score2))

for i in input:
    print(winningHand(i))