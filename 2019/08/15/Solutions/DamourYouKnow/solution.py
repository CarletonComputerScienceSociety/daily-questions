def rhythym_game_scoring_function(chart, presses):
    chart, presses = list(reversed(chart)), list(reversed(presses))

    score = 0
    while chart:
        note = chart.pop()
        while presses:
            press = presses.pop()
            if (note[0] - press[0] > 500): # Not active, skip
                continue
            if (abs(note[0] - press[0]) <= 200 and note[1] == press[1]):
                score += 100 * len(note[1])
            break
    return score


result = rhythym_game_scoring_function(
    [
        [1000, ['B']],
        [1500, ['A', 'C']],
        [2000, ['B', 'D']],
        [3000, ['A']],
        [3500, ['A']],
        [4000, ['D']],
        [4500, ['D']],
        [8000, ['A', 'B', 'C', 'D']]
    ],
    [
        [100, ['A']], # No active note in +/-500ms, ignore
        [900, ['B']], # -100ms, 100 points
        [1700, ['A', 'C']], # +200ms, 200 points 
        [2000, ['B', 'D']], # +0ms, 200 points
        [2800, ['A']], # -200ms, 100 points
        [3000, ['A']], # -500ms, Too early!
        [4000, ['D']], # +0ms, 100 points
        [4500, ['B']], # +0ms, Wrong button!
        [8300, ['A', 'B', 'C', 'D']] # +300ms, Too late!
    ]
)
print(result)



