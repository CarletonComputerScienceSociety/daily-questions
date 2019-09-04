function count(str, search) {
    const counts = {};
    for (s of search) {
        const matches = str.match(new RegExp(s, 'g'));
        counts[s] = matches ? matches.length : 0;
    }
    return counts;
}

        



