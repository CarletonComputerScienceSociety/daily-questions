function removeDuplicates(str) {
    return str.split('').reduce((a, c) => c == a[a.length-1] ? a : [...a, c], []).join('');
}
