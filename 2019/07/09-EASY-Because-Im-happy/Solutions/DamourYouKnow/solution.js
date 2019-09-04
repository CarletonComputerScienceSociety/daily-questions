function happy(number) {
    seen = new Set()
    while (number != 1 && !seen.has(number)) {
        seen.add(number);
        number = String(number).split('').map(Number).reduce((acc, cur) => {
            return acc + Math.pow(cur, 2)
        }, 0);
    }
    return number == 1;
}

console.log(happy(19));
console.log(happy(39));
