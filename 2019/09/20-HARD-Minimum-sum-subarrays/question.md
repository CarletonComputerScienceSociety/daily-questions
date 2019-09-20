# September 20, 2019 - Minimum sum subarrays [Hard]

Given an array of positive integers and a specified number of chunks, `m`, 
return the values of the array grouped into `m` chunks such that the largest 
of the sums of the `m` chunks is minimized.

Example:
```
Input:
array = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
```