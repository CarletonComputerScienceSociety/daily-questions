# September 5, 2019 - Password requirements [Medium]

You've been tasked with enforcing password requirements for your university's 
student portal. Write a function that takes a password string as input and 
validates it against the following password requirements:
- Password must not contain the following characters: "#,@&`$()/~\\^|<>=;.
- Password must not be longer than 15 characters.
- Password must be at least 8 characters long.
- Password must contain at least 1 lowercase character.
- Password must contain at least 1 numeric character.
- Password must contain at least 1 uppercase character.

Return true if the password is valid, otherwise return false.

Example:
```
Input: 'LukaN!ghtF3ver'
Output: true

Input: 'Password123'
Output: true

Input: 'Hunter2' // Too short
Output: false

Input: 'm0ngoiswebscale' // No uppercase
Output: false

Input: 'CorrectHorseBatteryStapl3'
Output: false // Too long

Input: 'DECO*27!'
Output: false // No lowercase

Input: 'Student!'
Output: false // No numeric

Input: 'DROP TABLE;'
Output: false // Restricted character
```