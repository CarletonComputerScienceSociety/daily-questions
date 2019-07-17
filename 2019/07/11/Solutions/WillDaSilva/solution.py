from functools import reduce

def permutations(x):
    f = lambda x,y: [a+[b] if isinstance(a, list) else [a]+[b] for a in x for b in y]
    r = reduce(f, [range(len(x))]*len(x))
    return (tuple(x[i] for i in j) for j in r if len(set(j)) == len(x))

