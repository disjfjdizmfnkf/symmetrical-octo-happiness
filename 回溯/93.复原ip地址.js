/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function (s) {
  const res = [];
  const len = s.length;
  if (len < 4 || len > 12) return res;

  function backtrack(combine, start = 0) {
    if (combine.length === 4) {
      //! 判断当前是否执行到最后了
      if (start === len) {
        res.push(combine.join("."));
      }
      return;
    }

    // 一次只使用一个到三个数字
    for (let i = 1; i <= 3; i++) {
      const sub = s.substring(start, start + i);
      //! 不能有前导0  比较字符串
      if (sub.length > 1 && sub[0] === "0") continue;
      // 不能超过255
      if (+sub > 255) continue;
      backtrack([...combine, sub], start + i);

      // 也可以使用这种写法，原则上就是在这块代码的最后不能改变原数组
      // combine.push(sub);
      // backtrack(combine, start + i);
      // combine.pop();
    }
  }
  backtrack([]);
  return res;
};
