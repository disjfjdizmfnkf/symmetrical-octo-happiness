/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const wind = new Set();
    let res = 0, l = 0;
    for (let r = 0; r < s.length; r++) {
        // 检查wind中有没有要添加的元素
        while (wind.has(s[r])) {
            wind.delete(s[l]);  //* 删除集合中的对象使用delete
            l++;  //! 放在while的最后
        };
        wind.add(s[r]);
        res = Math.max(res, r - l + 1);
    }
    return res;
};
