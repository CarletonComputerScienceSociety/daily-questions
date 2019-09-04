# August 15, 2019 - Rhythm game scoring [Medium]

In rythym games, charts are a collection of notes in a song 
that occur at specified points in time. A chart can be represented as an array 
of 2-tuples where the first item is the time in milliseconds since the song 
start where the note occurs and the second item is the sequence of buttons 
that the player must hit simultaneously.

Example of a chart:
```js
[
    [1000, ['B']],
    [1500, ['A', 'C']],
    [2000, ['B', 'D']],
    [3000, ['A']],
    [3500, ['A']],
    [4000, ['D']],
    [4500, ['D']],
    [8000, ['A', 'B', 'C', 'D']]
]
```

Charts are compared to the sequence of the player's inputs and are scored based 
on the player's ability to press the correct note sequences within a certain 
margin of time.

Example of an input sequnece:
```js
[
    [900, ['B']],
    [1700, ['A', 'C']],
    [2000, ['B', 'D']],
    [2800, ['A']],
    [3000, ['A']],
    [4000, ['D']],
    [4500, ['B']], 
    [8300, ['A', 'B', 'C', 'D']] 
]
```

We will examine a simple rythym game. In this game, 
notes are considered active within +/-500ms of the note's time. While a note is 
active it considers the input of the player and checks's if it is a hit or miss. 
Only the next note in the sequence can be active. If the next note is not 
active input from the player should be ignored.

A player misses a note if wrong button sequence is pressed, if the player is 
more than 200ms early or more than 200ms late, or if the player does not 
attempt to clear a note while it is active. If the player presses the correct 
button sequence within +/-200ms it is considered a hit.

When a player hits a note or presses a wrong button during the 500ms time 
frame where the next note is active, the note is cleared from the song's chart 
so that the player is not able to hit the same note twice. When comparing 
the chart to the user's input it is important to only ever consider the next 
note in the chart.

Hitting a note succesfully gives the player 100 points per button in the 
note. `[B]` is worth 100 points while `[A, B, C, D]` is worth 400 points. A 
miss is worth 0 points. Note that if the next note is `[A, B]` and the player 
only presses `[A]` it is still counted as a miss and is worth 0 points.

Given a chart and a player input sequence. Return the score the player 
has achieved.

Example:
```js
Chart = [
    [1000, ['B']],
    [1500, ['A', 'C']],
    [2000, ['B', 'D']],
    [3000, ['A']],
    [3500, ['A']],
    [4000, ['D']],
    [4500, ['D']],
    [8000, ['A', 'B', 'C', 'D']]
]

InputSequence = [
    [100, ['A']], // No active note in +/-500ms, ignore, don't clear the next note from chart
    [900, ['B']], // -100ms, 100 points
    [1700, ['A', 'C']], // +200ms, 200 points 
    [2000, ['B', 'D']], // +0ms, 200 points
    [2800, ['A']], // -200ms, 100 points
    [3000, ['A']], // -500ms, Too early!
    [4000, ['D']], // +0ms, 100 points
    [4500, ['B']], // +0ms, Wrong button!
    [8300, ['A', 'B', 'C', 'D']] // +300ms, Too late!
]

Output = 700
```


