def remove_invalid_parens(paren_string):
    def is_valid(paren_string):
        balance = 0 # 0 <=> balanced
        for x in paren_string:
            balance += (x == '(') - (x == ')')
            if 0 > balance:
                return False # unable to match unmatched ')'
        return 0 == balance
    bfs_level = {paren_string}
    while True:
        if valid := [x for x in bfs_level if is_valid(x)]:
            return valid
        bfs_level = {x[:i] + x[i+1:] for x in bfs_level for i in range(len(x))}

