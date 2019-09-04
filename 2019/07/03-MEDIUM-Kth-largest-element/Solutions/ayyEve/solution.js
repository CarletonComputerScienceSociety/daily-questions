function getK(array, k) {
    let temp = [];

    for (let i = 0; i < array.length; i++) {
        const x = array[i];
        temp[x] ? temp[x]++ : temp[x] = 1;
    }

    // remove undefineds
    temp = temp.filter(x=> {
        return x != undefined;
    });

    let newArray = [];
    for (let i = 0; i < temp.length; i++) {
        if (!temp[i]) continue;
        for (let n = 0; n < temp[i]; n++) {
            newArray.push(i+1);
        }
    }

    return newArray[newArray.length - k];
}
