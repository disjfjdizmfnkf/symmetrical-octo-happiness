/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if (strs.length === 0) return "";
    strs.sort();
    //! 错误: strs.sort((a, b) => a - b);  字符串相减 NaN
    //! 正确: strs.sort(); 字典排序
    //! 正确: strs.sort((a, b) => a.localeCompare(b)); // 字典排序
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