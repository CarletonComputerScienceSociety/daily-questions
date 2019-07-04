import itertools as it

def grid_search(grid):
    def grid_search_from_coord(grid, x, y):
        if 0 <= y < len(grid) and 0 <= x < len(grid[y]):
            check = yield (grid[y][x], x, y)
        else: check = yield (None, x, y)
        if check:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                yield from grid_search_from_coord(grid, x+dx, y+dy)
    for x, y in it.product(range(len(grid[0])), range(len(grid))):
        yield from grid_search_from_coord(grid, x, y)

def is_word_in_grid(grid, word):
    used = []
    i = f = 0
    searcher = grid_search(grid)
    current, x, y = next(searcher)
    while True:
        match = word[i] == current and (x, y) not in reversed(used)
        if match: f = 0; i += 1; used.append((x, y))
        else: f += 1
        if i == len(word): return True
        if f == 4:
            f = 0
            i = max(0, i - 1)
            try: del used[-1]
            except: pass
        try: current, x, y = searcher.send(match)
        except StopIteration: return False

