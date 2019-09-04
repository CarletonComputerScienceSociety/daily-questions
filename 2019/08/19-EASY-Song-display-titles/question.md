# August 19, 2019 - Song display titles [Easy]

Given an array of 2-tuples where the first item is a song title and the 
second item is a list of artists return an array of song display titles formatted 
as `<Artists> - <Song title>`. In the case where there are no artists return 
only the song title. In the case where there are two artists the artist string 
should be `<Artist 1> and <Artist 2>`. In the case where there are 3 or more 
artists the artist string should be `<Artist 1>, <Artist 2>, and <Artist n>`.


Example:
```python
Input = [
    ('Mamma Mia', ['ABBA']),
    ('Ghost Rule', ['DECO*27', 'Hatsune Miku']),
    ('Animals', ['Martin Garrix']),
    ('Remember The Name', ['Ed Sheeran', 'Eminem', '50 Cent']),
    ('404 Not Found', [])
]

Output = [
    'ABBA - Mamma Mia',
    'DECO*27 and Hatsune Miku - Ghost Rule',
    'Martin Garrix - Animals',
    'Ed Sheeran, Eminem, and 50 Cent - Remember The Name',
    '404 Not Found'
]
```
