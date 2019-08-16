def lps(s):
    result = ''
    for c in range(len(s)):
        palindrome = s[c]
        r_offset = 0
        if c < len(s) - 1 and s[c] == s[c+1]:
            palindrome += s[c+1]
            r_offset = 1
        for offset in range(1, min(c, len(s) - 1 - r_offset - c) + 1):
            if s[c-offset] == s[c+offset+r_offset]:
                palindrome = ''.join([s[c-offset], palindrome, s[c-offset]])
            else:
                break
        if len(palindrome) > len(result):
            result = palindrome
    return result

print(lps('abcddcbaeee'))

