/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const res = [];
    function backTrack(combine, l, r) {
        if (l === n && r === n) {
            res.push(combine);
        }
        if (l < n) {
            backTrack(combine + '(', l + 1, r);
        }
        if (l > r) {
            backTrack(combine + ')', l, r + 1);
        }
    }
    backTrack("", 0, 0);
    return res;
};