import itertools

def permutations(elements):
    return list(itertools.permutations(elements))

print(permutations({1, 2, 3}))