/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
  const res = [];
  function backtrack(combine, l = 0, r = 0) {
    if (l === n && r === n) res.push(combine);
    //! 添加左括号: l < n ; 添加右括号: l > r
    if (l < n) backtrack(combine + "(", l + 1, r);
    if (l > r) backtrack(combine + ")", l, r + 1);
  }
  backtrack("");
  return res;
};
