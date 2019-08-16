function flat(arr) {
    return arr.reduce((a, c) => a.concat(c));
}

console.log(flat([[1, 2, 3], [4, 5], [6], [], [7, 8, 9, 10]]));