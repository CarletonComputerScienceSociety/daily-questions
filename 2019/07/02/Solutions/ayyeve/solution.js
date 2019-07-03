function moveZeros2(array, zeroNum = 0) {
    return array.sort((n1, n2) => {
        if (n2 === zeroNum) return -1;
        else return 1;
    });
}
