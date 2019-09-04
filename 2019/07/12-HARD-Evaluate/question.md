# July 12, 2019 - Evaluate [Hard]

Given an expression string such as `"4 * (3 + 2)"` return the result of the 
expression.

The following operators must be supported:
- `+`: add
- `-`: subtract
- `*`: multiply
- `/`: divide

Values in the expression can be any positive or negative number. Decimals are 
allowed.

Additionally, you must follow the correct order of operations and handle 
the `(` and `)` parentheses.

Examples:
```
Input: "4 * (3 + 2)"
Output: 20

Input: "3"
Output: 3
```

**Note**:
Your solution must not be vulnerable to arbitrary code injection. (So no 
using eval).
