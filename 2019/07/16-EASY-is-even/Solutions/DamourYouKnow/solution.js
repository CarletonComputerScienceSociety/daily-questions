
function evenOdd1(arr) {
    return [...arr.filter((n) => n % 2 == 0), ...arr.filter((n) => n % 2 != 0)]
}

function evenOdd2(arr) {
    return arr.sort((a, b) => a % b);
}

function evenOdd3(arr) {
    // lol dependencies
    const isEven = require('is-even');
    const isOdd = require('is-odd');
    return [...arr.filter(isEven), ...arr.filter(isOdd)] 
}

console.log(evenOdd1([3,1,2,4]));