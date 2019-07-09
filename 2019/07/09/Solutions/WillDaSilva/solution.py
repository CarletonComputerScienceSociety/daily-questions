from functools import lru_cache

def digitize(n, base=10):
    if n == 0:
        yield 0
    while n:
        n, d = divmod(n, base)
        yield d

@lru_cache(None)
def is_happy_number(n):
    return n == 1 or n > 6 and is_happy_number(sum(x**2 for x in digitize(n)))

