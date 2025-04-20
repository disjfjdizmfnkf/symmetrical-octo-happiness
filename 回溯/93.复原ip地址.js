/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function (s) {
  const res = [];
  const combine = [];

  if (s.length > 12 || s.length < 4) return res;

  function backtrack(start = 0) {
    if (combine.length === 4) {
      if (start === s.length) {
        res.push(combine.join("."));
      }
      return;  //! 一种情况结束
    }
    //! 每次往后选取1-3个字符
    for (let i = 1; i <= 3; i++) {
      const sub = s.substring(start, start + i);
      //! 剪枝: 1. 大于255 2. 有前导0
      if (+sub > 255 || (sub.length > 1 && +sub[0] === 0)) continue;
      combine.push(sub);
      backtrack(start + i);
      combine.pop();
    }
  }
  backtrack();
  return res;
};
