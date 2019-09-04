import itertools as it

def tree_levels(tree, depth=None):
    powers = (2**x for x in it.islice(it.count(), depth))
    a, b = it.tee(it.accumulate(it.chain([0], powers)))
    for i, j in zip(a, it.islice(b, 1, None)):
        yield (x for x in it.islice(tree, i, j) if x is not None)

