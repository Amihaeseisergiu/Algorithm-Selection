export function binarySearch(array, el) {
    let m = 0;
    let n = array.length - 1;

    while (m <= n) {
        let k = (n + m) >> 1;
        let cmp = el - array[k];
        if (cmp > 0) {
            m = k + 1;
        } else if (cmp < 0) {
            n = k - 1;
        } else {
            return [k, k + 1];
        }
    }

    return [n, n + 1];
}