# August 29, 2019 - Connect Four

Connect Four is a game played between two players, red and blue. Each player 
takes turns droping a piece of their colour through the top of one of the 
columns of a vertical m x n grid. After a piece is placed it will fall down 
and occupy the lowest empty space. The goal of the game is for a player to 
form a line of four consecutive pieces of their colour either vertically, 
horizontally, or diagonally.

Given an incomplete Connect Four grid composed of integers where `0` represents 
an empty space, `1` represents a red piece, and `1` represents a blue piece, 
Return the array of column indices (starting from 0) that would result in a win 
for the red player.


Example:
```
Input: [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 2, 1, 0, 2],
    [1, 2, 1, 1, 2, 1, 1],
    [1, 1, 2, 2, 1, 2, 2],
    [1, 2, 2, 1, 2, 1, 1]
]

Output: [0, 2]
```