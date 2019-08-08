function minesweeper(board) {
    return board.map((row, i) => row.map((_, j) => {
        const near = [
            [1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]
        ].map((d) => [d[0]+i, d[1]+j]);
        return near.reduce((a, c) => a + ((board[c[0]] || [])[c[1]] || 0), 0);
    }));
}


const board = [
    [0, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 0, 0, 1]
]
console.log(minesweeper(board));