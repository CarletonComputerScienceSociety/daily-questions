# July 24, 2019 - Rectangle intersection [Medium]

Given an array of rectangles represented as 4-tuples where:
- t1 is x coordinate of the bottom left corner.
- t2 is the y coordinate of the bottom left corner.
- t3 is the width.
- t4 is the height.

Compute the intersection of the rectangle array.

Examples:
```
Input: [(0, 0, 10, 10)]
Output: (0, 0, 10, 10)

Input: [(0, 0, 10, 10), (5, 5, 10, 10)]
Output: (5, 5, 5, 5) 

Input: [(0, 0, 10, 10), (5, 5, 10, 10), (10, 10, 10, 10)]
Output: (10, 10, 0, 0)

Input: [(0, 0, 1, 1), (2, 2, 1, 1)]
Output: null
```

**Note**: If there is no valid intersection across all rectangles return null. 
The intersection may be a point or a line, in this case `0` is a valid value 
for width and height. 