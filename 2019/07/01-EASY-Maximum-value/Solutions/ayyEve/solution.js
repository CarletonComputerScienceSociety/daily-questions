function max(array) {
    let highest = 0;
    array.forEach(x => {
        highest = Math.max(highest, x);
    });
    return highest;
}
