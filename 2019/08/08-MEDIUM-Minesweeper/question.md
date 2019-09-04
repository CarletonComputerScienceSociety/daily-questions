# August 8, 2019 - Minesweeper [Medium]

Given an 2d array representing a minesweeper board where `0` represents an 
empty space and `1` represents a mine, return a new board where each cell 
represents the number of neighboring mines.

Note that diagonally adjacent cells are also considered neighbors.

Example:
```
Input:
[
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 1]
]

Output: 
[
    [2, 3, 2, 2],
    [1, 2, 3, 1],
    [3, 3, 3, 2],
    [0, 1, 1, 0]
]
```