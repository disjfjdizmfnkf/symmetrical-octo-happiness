/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const wind = new Set();
    let res = 0, l = 0;
    for (let r = 0; r < s.length; r++) {
        while (wind.has(s[r])) {
            wind.delete(s[l]);
            l++;
        };
        wind.add(s[r]);
        res = Math.max(res, r - l + 1);
    }
    return res;
};
