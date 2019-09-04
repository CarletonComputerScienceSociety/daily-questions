# July 22, 2019 - Working days [Easy]

Given a year integer, an array of regular days off that contain values from 
0 to 6. (0=Sunday, 1=Monday, ...), and an array of holiday date strings return 
an ordered array of working days for the year.

Example:
```
Input:
year = 2019
days_off = [0, 6]
holidays = ['2019-01-10']

Output:
[
    '2019-01-01',
    '2019-01-02',
    '2019-01-03',
    '2019-01-04', // Skip Sunday, Saturday
    '2019-01-07',
    '2019-01-08',
    '2019-01-09', // Skip Holiday
    '2019-01-11',
    '2019-01-14',
    '2019-01-15',
    ...,
    '2019-12-31'
]
```

**Note:**
All dates for input and output are `yyyy-mm-dd` formatted datestrings.
