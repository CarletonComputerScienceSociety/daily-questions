# August 12, 2019 - Pazaak

In Pazaak, two hands of of cards (with integer values ranging from -10 to 10) 
are compared. The winning hand is the hand with the total sum equal that is 
closest to 20, but not greater than 20. In the case where both hands are 
equal in value, the two hands are considered a tie. 

Pazaak hands are built by each player taking turns drawing cards until they 
stand, each player may also play a card from their side deck after each draw. 
Because of this, the two hands may have different sizes.

Write a function that takes two Pazaak hands as input and outputs the value of 
the winning hand. In the case of a tie, output `null` or the equivilant value 
for your language.

Examples:
```
Input: hand1 = [5, 10, 4], hand2 = [6, 6, 1, 2, 3]
Output: 19 (hand1 = 19, hand2 = 18)

Input: hand1 = [9, 9, 4, -2], hand2 = [10, 10]
Output: null (hand1 = 20, hand2 = 20)

Input: hand1 = [9, 8, 4], hand2 = [5, 6, 4]
Output: 15 (hand1 = 22, hand2 = 15, hand1 is over 20 so hand2 wins)
```