/**
 * @param {string} s
 * @return {string}
 */
var longestPalindrome = function(s) {
    let len = s.length;
    let res = '';
    if (len < 2) return s;
    for (let i = 0; i < len; i++) {
        //* 处理奇数和偶数长度
        helper(i, i);
        helper(i, i + 1);
    }
    function helper(m, n) {
        while (m >= 0 && n < len && s[m] === s[n]) {
            m--;
            n++;
        }
        //! n - m + 1 = 计算两个边界的长度 | n - m + 1 - 2 = 不计算两个边界
        if (n - m - 1 > res.length) {
            res = s.slice(m + 1, n); //! slice(start, end) 不包含end
        }
    }
    return res
};
