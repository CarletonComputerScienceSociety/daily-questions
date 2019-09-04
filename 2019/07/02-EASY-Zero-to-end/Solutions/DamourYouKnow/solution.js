function zeroesToEnd(arr) {
    return [...arr.filter(num => num != 0), ...arr.filter(num => num == 0)];
}
