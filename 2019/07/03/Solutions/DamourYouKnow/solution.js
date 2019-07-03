// O(n^2)
function kthLargest(arr, k) {
    return Math.min(...[...Array(k).keys()].map(() => arr.splice(arr.indexOf(Math.max(...arr)), 1)[0]));
}
