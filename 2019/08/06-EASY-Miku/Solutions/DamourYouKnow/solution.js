function miku(n) {
    for (i = 1; i <= n; i++) {
        const val = (x) => {
            if (x % 9 == 0) return 'Miku';
            else if (x % 3 == 0) return 'Mi';
            return `${x}`;
        }
        console.log(val(i));
    }
}

miku(39);