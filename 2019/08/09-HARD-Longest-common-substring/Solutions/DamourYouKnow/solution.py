def lcs(a, b):
    result = ''
    for c in range(len(a)):
        for c_end in range(c, len(a)):
            check = a[c:c_end]
            if check in b and len(check) > len(result):
                result = check
    return result


print(lcs('abcdddefg', 'aabbccddd')) # cddd