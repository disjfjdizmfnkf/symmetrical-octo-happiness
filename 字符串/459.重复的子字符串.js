/**
 * @param {string} s
 * @return {boolean}
 */
var repeatedSubstringPattern = function (s) {
  //NOTE: 将两个字符串拼接起来, 将首尾字符删除, 如果是重复字符串一定有s在中间
  let ss = s + s;
  // 删除首尾字符
  ss = ss.slice(1, ss.length - 1);
  return ss.includes(s);
};
