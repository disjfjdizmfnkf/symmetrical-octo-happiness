/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";
    strs.sort();
    let s = strs[0];
    let l = strs[strs.length - 1];
    let i = 0;
    while (i < l.length) {
        if (s[i] !== l[i]) {
            break;
        }
        i++;
    }
    return s.substring(0, i);
};