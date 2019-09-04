function countJewels(jewels, stones) {
    return stones.split('').reduce((a, c) => jewels.includes(c) ? a + 1 : a, 0);
}

console.log(countJewels('aA', 'aAAbbbb'));
console.log(countJewels('z', 'ZZ'));

