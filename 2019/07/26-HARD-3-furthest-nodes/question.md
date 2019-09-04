# July 26, 2019 - 3 furthest nodes [Hard]

Given a graph with weighted edges and nodes with values `{0, 1, ..., n}`, find 
the 3 furthest nodes such that the total distance between them is 
maximized.

The input graph is represented as an adjacency matrix such that `matrix[i][j]` 
represents the distance between nodes `i` and `j`. This value will be null if 
`i` and `j` are not neighbors.

The distance between two nodes is computed as the length of the shortest path 
between them.

Example:
```
Input: 
[
    [0, 3, 2, null],
    [3, 0, 2, null],
    [2, 2, 0, 1],
    [null, null, 1, 0]
]

Output: [0, 1, 3]
```

**Note:** Assume that the number of nodes in the graph is >= 3.