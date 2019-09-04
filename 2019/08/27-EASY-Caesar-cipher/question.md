# August 27, 2019 - Caesar Cipher [Easy]

The caesar cipher can be used to encrypt a string of characters in the range 
`A-Z` by shifting characters to the right `k` places, where `k` is the key of 
the cipher. The character `'E'` shifted right by 2 would become `'G'`.
A caesar encrypted string can be decrypted by shifting each character `k` 
places to the left. Spaces are not transformed by this cipher.

The cipher is modular so `'B'` shifted to the left by 3 is `'Y'`.

Given a caesar encrypted strsing string of uppercase characters and a key, `k`, 
return the decrypted string. Expect `k` to always be a positive integer.

Example:
```
Input: 'DRO MKCDVO CRYEVN LO EZQBKNON KC CYYX KC ZYCCSLVO', key = 10
Input: 'KHOOR HYHUBRQH LP VFRWW SUHVLGHQW RI GRPLQRV SLCCD', key = 3
Input: 'FTUE FTUZS PQXQFQP FTDQQ YAZFTE AR IADW', key = 12

Output: A super secret human readable string
```
