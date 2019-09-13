# September 13, 2019 - Wildcard matching [Hard]

Given a string and a pattern, implement wildcard pattern matching with support 
for '?' and '*' where:
- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).

Examples:
```
Input: string = "python" and pattern = "javascript" 
Output: false

Input: string = "python" and pattern = "py*n"
Output: true

Input: string = "python" and pattern = "?yt*n"
Output: true

Input: string = "python" and pattern = "?yt*nn"
Output: false
```