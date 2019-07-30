function removeDuplicates(str) {
    const remove = (arr) => {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] == arr[i-1]) {
                return remove([...arr.slice(0, i-1), ...arr.slice(i+1)]);
            }
        }
        return arr;
    };

    return remove(str.split('')).join('');
}
