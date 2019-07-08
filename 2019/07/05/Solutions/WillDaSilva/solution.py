import itertools as it

def longest_consecutive_seq_len(a):
    s = set(a)
    best_len = 0
    for x in a:
        if x not in s: continue
        current_len = 1
        for step in (1, -1):
            for i in it.count(x+step, step):
                if i in s: current_len += 1
                else: s -= set(range(x, i, step)); break
        best_len = max(best_len, current_len)
    return best_len
