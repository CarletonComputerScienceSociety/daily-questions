def permutations(elems):
    if len(elems) == 0:
        return []
    if len(elems) == 1:
        return [elems]

    perms = []
    for e in range(len(elems)):
        perms += [[elems[e]] + p for p in permutations(elems[:e] + elems[e + 1:])]
    return perms


print(permutations([1,2,3]))
