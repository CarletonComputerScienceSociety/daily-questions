function rot(arr, k){ if{k>arr.length) k-=arr.length; return arr.slice(k, arr.length).concat(arr.slice(0, k)); }
