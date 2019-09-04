# July 9, 2019 - Because I'm Happy [Easy]

Write an algorithm to determine if a number is happy.

A happy number is defined by the following process:

Starting with any positive integer, replace the number by the sum of 
the square of it's digits and repeat the process until the number equals 
1 (where it will stay), or it loops endlessly in a cycle which does not 
include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
```
Input: 19
Output: True

Explanation:
   1^2 + 9^2 = 82
   8^2 + 2^2 = 68
   6^2 + 8^2 = 100
   1^2 + 0^2 + 0^2 = 1
```