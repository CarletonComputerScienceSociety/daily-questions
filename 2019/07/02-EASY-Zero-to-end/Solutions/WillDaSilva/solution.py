def move_zeros_to_end(a):
    return sorted(a, key=lambda x: 0 if x else float('inf'))

