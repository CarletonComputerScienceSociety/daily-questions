# September 25, 2019 - Check digit [Medium]

The last number in a 10-digit ISBN number is the check digit. In a valid 
ISBN number, this check digit can be verified by applying the following 
process:
    1. Multiply each digit, including the check digit, by it's position in 
    order from right to left.
    2. Sum the results of each product together.
    3. Compute the remainder of the product sum when it is divided by 11.

If the result of this process is equal to 0, the ISBN number is 
valid.

For example the product sum of the ISBN number 0-201-53082-1 is computed as 
follows:
```
1(1) + 2(2) + 3(8) + 4(0) + 5(3) + 6(5) + 7(1) + 8(0) + 9(2) + 10(0) = 99 
```

The reminder of 99 divided by 11 is 0, so the ISBN number is valid.

Given an ISBN number string return true if the number is valid, otherwise 
return false.

Example
```
Input: 0-201-53082-1
Output: true
```
