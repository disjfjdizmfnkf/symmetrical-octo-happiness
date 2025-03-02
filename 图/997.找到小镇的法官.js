/**
 * @param {number} n
 * @param {number[][]} trust
 * @return {number}
 */
var findJudge = function(n, trust) {
    const inDegress = new Array(n).fill(0);
    const outDegress = new Array(n).fill(0);
    for (const i of trust) {
        inDegress[i[1] - 1]++;
        outDegress[i[0] - 1]++;
    }
    for (let i = 0; i < n; i++) {
        if (inDegress[i] === n - 1 && outDegress[i] === 0) {
            return i + 1;
        }
    }
    return -1;
};