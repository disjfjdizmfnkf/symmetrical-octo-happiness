/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const res = [];
  function backtrack(combine, l = 0, r = 0) {
    if (l === n && r === n) res.push(combine);
    //! 添加左括号: l < n ; 添加右括号: l > r 右括号比左括号多了就闭不上了
    // 左括号小于n时都可以添加左括号
    if (l < n) backtrack(combine + "(", l + 1, r);
    if (l > r) backtrack(combine + ")", l, r + 1);
  }
  backtrack("");
  return res;
};

/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const res = [];
  const combine = [];

  function backTrack(l, r) {
    if (l === n && r === n) res.push(combine.join(''));
    if (l < n) {
      combine.push('(');
      backTrack(l + 1, r);
      combine.pop();
    }
    if (r < l) {
      combine.push(')');
      backTrack(l, r + 1);
      combine.pop();
    }
  }
  backTrack(0, 0);
  return res;
};
