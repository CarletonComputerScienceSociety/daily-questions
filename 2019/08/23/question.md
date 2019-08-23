# August 23, 2019 - Phrase building

A phrase is a collection of words seperated by spaces. The distance between two 
words is measured as the minimum number of the following steps required to 
transform one word to the other:
- Insertion of a new character
- Removal of a character
- Replacement of a character

For example, `hungry` can be transformed into `angry` in 2 steps.
- Remove `h` at index `0` -> `ungry`.
- Replace `u` at index `0` with `a` -> `angry`.

Given a phrase and a list of syllables, return a new phrase such that 
each word is replaced by the combination of syllables that results in the 
mininum distance between the syllable combination and the original word.

You may assume that words are all lowercase and containing only characters in 
the range `a-z`.

```
Input: 
phrase = 'blue hair blue tie hiding in your wifi'
syllables = [
    'blu',
    'ha',
    'ai',
    'di',
    'ing',
    'ti',
    'hi',
    'yo',
    'ii',
    'fi'
]

Output: 'blu ai blu ti hiing ii yo hifi'
```